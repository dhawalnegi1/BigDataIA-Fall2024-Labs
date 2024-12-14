.PHONY: install build run-app1 run-app2 clean run-all

POETRY = poetry
UVICORN = $(POETRY) run uvicorn
main = fastapi_demo.main:app
jwt = fastapi_demo.jwt_demo:app

install:
	$(POETRY) install
build:
	$(POETRY) check
run-main:
	$(UVICORN) $(main) --reload --port 8000
run-jwt:
	$(UVICORN) $(jwt) --reload --port 8001
clean:
	rm -rf __pycache__
run-all:
	$(MAKE) -j2 run-main run-jwt