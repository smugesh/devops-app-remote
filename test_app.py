# new_app.py

def add(a, b):
	return a + b;


def test_add():
	assert add(2, 3) == 5
	assert add(-1, 1) == 0
	print("All Tests Passed")


if __name__ == "__main__":
	test_add()