from fastapi import Depends, FastAPI, HTTPException, status
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user
from auth.routes import router as auth_router

from .database import engine, get_db
from .models import Base, Item
from .models import User as UserModel
from .schemas import ItemBase, ItemCreate, ItemUpdate

# Initialize FastAPI application
app = FastAPI(title="Cyberpunk Inventory Management System")

# Include authentication routes from the auth module
app.include_router(auth_router, prefix="/auth", tags=["auth"])

# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)


@app.get("/items", response_model=Page[ItemBase], status_code=200)
def read_items(
    db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)
):
    """
    Retrieve a paginated list of items.
    This endpoint supports pagination and is accessible only to authenticated users.
    """
    items = db.query(Item).all()
    return paginate(items)


@app.get("/items/{item_id}", response_model=ItemBase, status_code=200)
def read_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Retrieve a single item by its ID.
    Returns a 404 error if the item is not found.
    This endpoint is accessible only to authenticated users.
    """
    item = db.query(Item).filter(Item.id == item_id).first()  # Query item by ID
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/item", response_model=ItemBase, status_code=status.HTTP_201_CREATED)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Create a new item.
    Checks for existing items with the same name and raises an error if found.
    This endpoint is accessible only to authenticated users.
    """
    try:
        existing_item = (
            db.query(Item).filter(Item.name == item.name).first()
        )  # Check for duplicates
        if existing_item:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="An item with this name already exists.",
            )
        new_item = Item(**item.model_dump())  # Create new item
        db.add(new_item)
        db.commit()
        return new_item

    # Rollback in case of an error
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e


@app.put("/item/{item_id}", response_model=ItemBase, status_code=status.HTTP_200_OK)
def update_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Update an existing item by its ID.
    Returns a 404 error if the item is not found.
    This endpoint is accessible only to authenticated users.
    """
    db_item = (
        db.query(Item).filter(Item.id == item_id).one_or_none()
    )  # Query item by ID
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    # Update item attributes, iterate over all attributes
    for var, value in vars(item).items():
        # Update the corresponding attribute in the db_item if value is not None
        setattr(db_item, var, value) if value else None

    try:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e

    return db_item


@app.delete("/item/{item_id}", response_model=ItemBase, status_code=status.HTTP_200_OK)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """
    Delete an item by its ID.
    Returns a 404 error if the item is not found.
    This endpoint is accessible only to authenticated users.
    """
    item = db.query(Item).filter(Item.id == item_id).first()  # Query item by ID
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return item



# Add pagination support to the application
add_pagination(app)
