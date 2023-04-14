# Design Patterns

> "Are solutions to common problems in software design. Each pattern is like a blueprint that you can customize to solve a particular design problem." Refactoring Guru

## Types

1. Creational

   > Are designed for the instantiation of classes. They can be either class-creation patterns or object-creational patterns.

	* Factory Method

      > Used to create concrete implementations of a common interface. This pattern suggest that you replace direct object constructions calls with calls to a special factory method.

      **Logic**

       i. The `Product` declares the interface, which is common to all objects that can be produced by the `creator` and its subclasses.

       ii. Concrete Products are different implementations of the product interface.

       iii. The `Creator` class declares the factory method that returns new product objects.

       iv. Concrete creators override the base factory method so it returns a different type of product.

       The creator returns the concrete implementation according to the value of the parameter to the client, and the client uses the provided object to complete its task.

      The Diagram
      ---

       ![Factory Method Pattern](/diagrams/factory-method-pattern.svg)

   * Builder

      > It allows you to construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

      **Logic**

      The pattern organizes object construction into a set of steps. To create an object, you execute a series of these steps on a builder object. The important part is that you don't need to call all of the steps. You can call only those steps that are necessary for producing a particular configuration of an object.

       i. The Builder interface declares product construction steps that are common to all types of builders.

       ii. Concrete builders provide different implementation of the construction steps. Concrete builders may produce products that don't follow the common interface.

       iii. Products are resulting objects. Products constructed by different builders don't have to belong to the same class hierarchy or interface.

       iv. The Director class defines the order in which to call construction steps, so you can create and reuse specific configurations of products.

       v. The Client must associate one of the builder objects with the director. Usually, it's done just once, via parameter of the director's constructor. Then the director uses that builder object for all further construction. However, there's an alternative approach for when the client passes the builder object to the production method of the director. In this case, you can use a different builder each time you produce something with the director.

      The Diagram
      ---

       ![Factory Method Pattern](/diagrams/builder-pattern.svg)

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
