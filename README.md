# pythonHakrnk

A collection of Python practice solutions covering core Python concepts and NumPy operations, primarily based on [HackerRank](https://www.hackerrank.com/) challenges.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
  - [String Manipulation](#string-manipulation)
  - [Lists, Tuples & Sets](#lists-tuples--sets)
  - [NumPy Operations](#numpy-operations)
  - [Basic Python](#basic-python)
- [Running the Solutions](#running-the-solutions)
- [Topics Covered](#topics-covered)

---

## Overview

This repository contains standalone Python scripts, each solving a specific programming challenge. The solutions are organized by topic and demonstrate common Python patterns and NumPy usage.

---

## Prerequisites

- **Python 3.x**
- **NumPy** (required for all NumPy-related scripts)

Install NumPy with:

```bash
pip install numpy
```

---

## Repository Structure

### String Manipulation

| File | Description |
|------|-------------|
| [`sWAPcASE.py`](sWAPcASE.py) | Swaps the case of every character in a string (uppercase ↔ lowercase). |
| [`StringFormatting.py`](StringFormatting.py) | Prints numbers from 1 to N in decimal, octal, hexadecimal, and binary, right-justified. |
| [`StringSplitAndJoin.py`](StringSplitAndJoin.py) | Splits a string on spaces and rejoins the tokens with hyphens. |
| [`StringValidators.py`](StringValidators.py) | Checks a string for alphanumeric, alphabetic, digit, lowercase, and uppercase characters. |
| [`FindAString.py`](FindAString.py) | Counts how many times a substring appears within a string (case-sensitive). |
| [`Mutations.py`](Mutations.py) | Replaces a character at a given index in a string. |
| [`TextAlignment.py`](TextAlignment.py) | Draws an ASCII art "H" pattern using `rjust`, `ljust`, and `center` string methods. |
| [`TextWrap.py`](TextWrap.py) | Wraps a long string to a specified maximum width by inserting newlines. |
| [`WhatSYourName.py`](WhatSYourName.py) | Accepts a first and last name and prints a personalized greeting. |
| [`DesignerDoorMat.py`](DesignerDoorMat.py) | Generates a decorative door-mat pattern with a "WELCOME" centred message. |

### Lists, Tuples & Sets

| File | Description |
|------|-------------|
| [`Lists.py`](Lists.py) | Processes a sequence of list commands (insert, append, remove, sort, pop, reverse, print). |
| [`Tuples.py`](Tuples.py) | Creates a tuple from user input and prints its hash value. |
| [`IntroductiontoSets.py`](IntroductiontoSets.py) | Computes the average of the unique elements in an array by converting it to a set. |
| [`SymmetricDifference.py`](SymmetricDifference.py) | Placeholder for a symmetric-difference set exercise. |

### NumPy Operations

| File | Description |
|------|-------------|
| [`Arrays.py`](Arrays.py) | Converts a space-separated string of numbers into a NumPy float array and reverses it. |
| [`ArrayMathematics.py`](ArrayMathematics.py) | Demonstrates element-wise arithmetic on 2-D NumPy arrays (add, subtract, multiply, floor-divide, mod, power). |
| [`Concatenate.PY`](Concatenate.PY) | Vertically stacks multiple NumPy arrays using `numpy.vstack()`. |
| [`EyeandIdentity.py`](EyeandIdentity.py) | Creates and displays identity matrices using `numpy.eye()`. |
| [`FloorCeilandRint.py`](FloorCeilandRint.py) | Applies `numpy.floor()`, `numpy.ceil()`, and `numpy.rint()` to an array. |
| [`ShapeandReshape.py`](ShapeandReshape.py) | Reads nine numbers and reshapes them into a 3 × 3 NumPy array. |
| [`TransposeandFlatten.py`](TransposeandFlatten.py) | Transposes a 2-D NumPy array and then flattens it to 1-D. |
| [`ZerosandOnes.py`](ZerosandOnes.py) | Creates NumPy arrays filled with zeros and ones using `numpy.zeros()` and `numpy.ones()`. |

### Basic Python

| File | Description |
|------|-------------|
| [`PrintFunction.py`](PrintFunction.py) | Prints integers 1 through N as a single concatenated string without spaces. |

---

## Running the Solutions

Each script is self-contained and can be run directly from the command line:

```bash
python <filename>.py
```

**Example:**

```bash
python sWAPcASE.py
```

Many scripts read input interactively. Supply the required values when prompted, or pipe them from a file:

```bash
echo "Hello World" | python sWAPcASE.py
```

---

## Topics Covered

- **Core Python**
  - String methods (`split`, `join`, `center`, `ljust`, `rjust`, `islower`, `isupper`, `isalpha`, `isdigit`, `isalnum`)
  - List operations (insert, append, remove, sort, pop, reverse)
  - Tuples and hashing
  - Sets and set operations
  - String formatting (f-strings, format specifiers for octal, hex, binary)
  - Text wrapping and alignment

- **NumPy**
  - Array creation (`numpy.array`, `numpy.zeros`, `numpy.ones`, `numpy.eye`)
  - Array manipulation (`numpy.flip`, `numpy.vstack`, `numpy.transpose`, `.flatten`, `.reshape`)
  - Element-wise arithmetic (`numpy.add`, `numpy.subtract`, `numpy.multiply`, `numpy.floor_divide`, `numpy.mod`, `numpy.power`)
  - Rounding functions (`numpy.floor`, `numpy.ceil`, `numpy.rint`)
