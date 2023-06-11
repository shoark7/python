# Async IO 란

## 개요
async IO는 기본적으로 concurrent programming design
* Concurrency: 병행, 복수의 작업의 전체 실행 기간이 일부 겹침.
* threading: 복수의 threading가 차례로 작업을 실행. 하나의 프로세스는 복수의 thread를 가질 수 있음. IO-bound job에 유용.
* Parellism: 병렬, 복수의 operation을 "동시"에 실행
* multiprocessing: parallelism을 실현하는 하나의 방법, 작업을 여러 CPU 코어로 분산해 실행. CPU-bound job에 유용.

---

asynIO: concurrent code를 짜기 위한 라이브러리. It's not a form of threading nor multiprocessing. **It's a single process, single thread design.** It uses 'cooperative multitasking'. 

asyncIO의 특징은 'asynchronous'하다. 이 뜻은 무슨 뜻일까?
* Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
* Asynchronous code facilitates concurrent execution. To put it differently, asynchronous code gives the look and feel of concurrency.


## Python's asyncio feature


### terminology
* coroutine: return에 다다르기 전에 자신의 실행을 정지하고 비간접적으로 제어를 다른 coroutine에 전달할 수 있는 함수
* async def: python에서 함수가 `native coroutine`, 또는 `asynchronous generator`라고 선언 
* await: cede function control back to the event loop. `await` 키워드는 python에 현재 coroutine의 실행을 멈추고 내가 실행하는 작업이 끝날 때까지 기다려라 - 그동안 다른 일을 하렴.
* event loop: `while True`과 같이 생각할 수 있으며, coroutine을 모니터링하고 idle한 task를 잡아 실행할 수 있는 역할. 
    - `asyncio.run()`이 이벤트 루프를 실행해 실행을 명령하는 command


## python asyncio design patterns

### 1. Chaining coroutines
asyncio.gather를 통해 모든 task를 대기. 실행시간은 MAX(tasks)


### 2. Queueing coroutines
consumer, producer 관계가 있고 이 둘이 독립적일 때 연결해 사용할 수 있음.

```
A Future-like object that runs a Python coroutine. Not thread-safe.

Tasks are used to run coroutines in event loops. If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion of the Future. When the Future is done, the execution of the wrapped coroutine resumes.

Event loops use cooperative scheduling: an event loop runs one Task at a time. While a Task awaits for the completion of a Future, the event loop runs other Tasks, callbacks, or performs IO operations.

Use the high-level asyncio.create_task() function to create Tasks, or the low-level loop.create_task() or ensure_future() functions. Manual instantiation of Tasks is discouraged.

---

Task는 Future같은 객체로, python coroutine을 실행한다.

Task는 event loop에서 coroutine을 실행하는 데 사용된다. coroutine이 Future에서 대기하면, Task는 코루틴의 실행을 중단하고 Future의 완료를 기다린다. Future가 끝나면 wrapped된 coroutine이 재개된다.

event loops는 cooperative scheduling을 사용한다. 죽, event loop은 한 번에 한 task를 실행한다. task가 Future의 완료를 대기하는 동안, event loop은 다른 task, callback, IO를 실행한다. task를 생성하는 고수준 api는 `asyncio.create_task`이다.
```

```
In summary, coroutines are the building blocks of asynchronous code, defining units of work that can be scheduled and run concurrently. Tasks represent the execution of coroutines and provide additional features and control for managing and interacting with coroutines within an event loop.
```

```
In Python's asyncio framework, a Future object is another fundamental concept used for managing the execution of asynchronous code. A Future represents a result that may not be available yet but will be resolved at some point in the future. It acts as a placeholder for a value that will be computed or set later.

A Future is similar to a Task but lacks some of the higher-level features and control provided by a Task. It serves as a lower-level primitive for handling the state and result of a computation. A Task is actually a subclass of Future with additional functionality built on top of it.

A Future can be in one of three states:

Pending: The Future is waiting for a result.
Completed: The Future has a result or an exception.
Cancelled: The Future was cancelled before it could complete.
You can interact with a Future object in various ways:

Setting a result or an exception: You can set a value or an exception on a Future using the set_result(result) or set_exception(exception) methods, respectively. This marks the Future as completed.

Retrieving the result: You can retrieve the result of a Future using the result() method, which returns the value if it's available. If the Future is still pending, this method will block until the result is available. You can also use yield from or await to pause the execution of a coroutine until the result is ready.

Cancelling a Future: You can cancel a Future by calling the cancel() method. This will transition the Future into the cancelled state. If the computation is already complete, this call has no effect.

Future objects are often used when you need more fine-grained control over the execution and management of asynchronous operations, such as handling callbacks or combining multiple asynchronous operations manually.
```