# Design Patterns

> "Are solutions to common problems in software design. Each pattern is like a blueprint that you can customize to solve a particular design problem." Refactoring Guru

## Types

1. Creational

   > Are designed for the instantiation of classes. They can be either class-creation patterns or object-creational patterns.

  * Factory Method

  > Used to create concrete implementations of a common interface. This pattern suggest that you replace direct object constructions calls with calls to a special factory method.⋅⋅

  *Logic*

    i. The `Product` declares the interface, which is common to all objects that can be produced by the `creator` and its subclasses.

    ii. Concrete Products are different implementations of the product interface.

    iii. The `Creator` class declares the factory method that returns new product objects.

    iv. Concrete creators override the base factory method so it returns a different type of product.

    The creator returns the concrete implementation according to the value of the parameter to the client, and the client uses the provided object to complete its task.

1. Structural
1. Behavior

## Setup

1. Create virtual environment

```
python -m venv venv

# Active the environment (Windows)
.\venv\Scripts\activate
```

2. Install dependencies

```
python -m pip install -r requirements.txt
```

3. Update `requirements.txt` file

```
python -m pip freeze > requirements.txt
```
