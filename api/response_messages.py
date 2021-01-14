from enum import Enum


class ResponseMessage(Enum):
	INCORRECT_REVIEW_FORMAT_400 = {"message": 'Some content in new review is missed!'}
	PRODUCT_NOT_FOUND_400 = {"message": "Product with this ID is not found!"}
	NEW_REVIEW_CREATED_201 = {"message": 'The new review added!'}
