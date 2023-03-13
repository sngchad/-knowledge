# Async

1. [Coroutines, tasks, futures](#Coroutines,-tasks,-futures)

2. [Event loop](#Event-loop)

3. [Schedule call back (call_soon)](#Schedule-call-back-(call_soon-/-call_later))

4. [Chaining coroutines](#Chaining-coroutines)

5. [QueueAsync generators](#QueueAsync-generators)

6. [ThreadPoolExecutor](#ThreadPoolExecutor)

## Coroutines, tasks, futures

> Coroutines, Tasks, and Futures are **Awaitable** objects

> **_Coroutine_** is subroutine, declared with the async/await syntax
1. A coroutine function: an async def function;
2. A coroutine object: an object returned by calling a coroutine function.

> **_Tasks_** are used to schedule coroutines concurrently.

> A **_Future_** is a special low-level awaitable object that represents an eventual result of an asynchronous operation.


## Event loop

## Schedule call back (call_soon / call_later)

## Chaining coroutines

## QueueAsync generators

## ThreadPoolExecutor