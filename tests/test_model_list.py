from flask_testing import TestCase
from flask import url_for
from os import getenv


from app import Paints, app, newentry
from app import db, Models



class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
        app.config['SECRET_KEY'] = getenv("SECRET_KEY")
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        return app
    
    def setUp(self):
        db.create_all()

        test_paint = Paints(paint_name = "Test Paint", needed = True)
        db.session.add(test_paint)
        db.session.commit()

        test_model = Models(model_name = "Test Model", added = True, paint_id = test_paint.id)
        db.session.add(test_model)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_page_get(self):
        response = self.client.get(url_for("index"))
        self.assertIn(b"Test Model", response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_page_get(self):
        response = self.client.get(url_for("delete"))
        self.assertIn(b"Test Model", response.data)
        self.assertEqual(response.status_code, 200)

    def test_add_page_get(self):
        response = self.client.get(url_for("add"))
        self.assertIn(b"Test Model", response.data)
        self.assertEqual(response.status_code, 200)

    def test_newentry_page_get(self):
        response = self.client.get(url_for("newentry"))
        self.assertEqual(response.status_code, 200)

class TestCreate(TestBase):
    def test_paint_create(self):
        response = self.client.post(
            url_for("newentry"),
            data = {"new_paint":"Test Paint"},
            follow_redirects=True
            )

    def test_model_create(self):
        response = self.client.post(
            url_for("newentry"),
            data = {"new_model":"Test Model"},
            follow_redirects=True
            )

class TestDelete(TestBase):
    def test_delete_model(self):
        response = self.client.get(url_for("delete", id=1))
        num_models = Models.query.count()
        self.assertEqual(num_models, 1)

    def test_delete_paint(self):
        response = self.client.get(url_for("delete", id=1))
        num_paints = Paints.query.count()
        self.assertEqual(num_paints, 1)
