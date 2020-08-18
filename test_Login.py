import pytest
@pytest.yield_fixture()
def setup():
	print("OPening URL to Login")
	yield
	print("Closing browser after login")
	
def test_loginbyemail(setup):
	print("this is login by email test")
	
def test_loginbyfb(setup):
	print("this is login by facebook test")