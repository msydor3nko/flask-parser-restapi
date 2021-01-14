class ProductException(Exception):
	pass


class ProductNotFoundError(Exception):
	pass


class ReviewException(Exception):
	pass


class ReviewMissedDataError(KeyError):
	pass
