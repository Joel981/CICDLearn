from app.models import ExampleModel

def test_get_data():
    model = ExampleModel()
    data = model.get_data()
    assert data == {"name": "Sample Data"}
