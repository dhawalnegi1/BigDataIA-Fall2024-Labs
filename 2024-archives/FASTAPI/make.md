Make ->
    A build automation tool to streamline repetitive tasks.
    Commonly used for compiling code, running tests, managing dependencies, and more.
    Helps standardize project workflows across environments.

Install Make ->
    sudo apt update
    sudo apt install make

Purpose of Makefile ->
    Define reusable commands to manage your FastAPI project.
    Simplify running multiple FastAPI apps with make.

Basic Structure ->
    Targets: Commands like install, build, run-app1, etc.
    Dependencies: Files or other tasks that should run before a target.
    Commands: Shell commands to execute for each target.

Install Dependencies ->
    make install
    make build
    make run-main
    make run-jwt
    make run-all