from api import app, db
from api.models import Product, Review


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Product': Product,
        'Review': Review,
    }
