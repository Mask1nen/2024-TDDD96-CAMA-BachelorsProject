from django.test import TestCase

# Create your tests here.
class TestClass:
    def start(self):
        x = "this"
        return x

    def test(self):
        sentence = self.start()
        assert sentence == "not this"