# Queue Data Structure

## A Basic Queue

You should implement a Queue that offers the following functions:

* `enqueue` adds an element to the end of the queue
* `dequeue` removes and returns the front element of the queue

Beyond those essentials, implement the following:

* `count` returns the number of elements in the queue
* `peek` returns the value of the front element without removing it
* `last` returns the value of the last element without removing it
* `empty` returns a true if the queue is empty, false if not

### Implementation Challenge

Your implementation language might already have a `Queue` data structure or `Array` functions that do all the hard work for you.

But what if, instead of using those, you implemented your `Queue` using a `LinkedList`?

It would be wise to implement once the easy way to make sure you understand everything, then reimplement using the `LinkedList`.

## Priority Queue

Now build on your `Queue` implementation by turning it into a `PriorityQueue`.

Let's explore the problem with an airport using a priority queue to manage which flights get to take off.

### Prerequisite

Implement a data container `Plane` that has the following attributes:

* `name` like `"UA352"`
* `expected_departure` in a number of minutes from midnight, like `510` for 8:30AM
* `expected_landing` in a number of minutes from midnight, like `615` for 10:15AM

### Round 1

Implement a PQ that works like this:

* When we enqueue, we pass in two values -- the priority number and the element itself (ex: `enqueue(2, obj)` where `obj` is a reference to a `Plane` instance)
* When we call the `.next` method, we are returned the front-priority plane in the PQ. The plane is removed from the PQ.
* When we call the `.peek` method, we get a reference to the front-priority plane in the PQ without altering the PQ.
* When we call `.status`, we are returned a snapshot of the current PQ status using a hash/dictionary where each key is the priority level and the value is the number of planes in that priority level:

```
{
  0 => 4,
  1 => 2,
  2 => 12,
  3 => 6,
  4 => 5,
  5 => 0
}
```

### Round 2

Improve your PQ to offer the following features:

* A `total_count` method which returns the total number of planes across all levels of the PQ
* A `queue_wait` method which is given a reference to a single plane and returns the total number of planes ahead of it in the PQ

### Round 3

Now we will implement a concept of time in the PQ:

* Add a `current_time` attribute to the PQ which tracks the current time in minutes since midnight
* Add a `tick(i)` method to the PQ which advances the `current_time` by `i` minutes

Then understand that our queue levels represent the following business rules:

- Level 0: “Override” - the plane was put in this level manually
- Level 1: “Nearly On-Time” - the plane is more than zero but less than 15 minutes late in taking off
- Level 2: “Recoverable Late” — the plane is more than 15 minutes late in taking off but has a flight time long enough to make up the time. A plane can make up 20% of expected flight time in the air.
- Level 3: “Well On-Time” — the plane's scheduled take-off time is in the future
- Level 4: “Irrecoverable Late” — the plane is late and on-time landing is not recoverable
- Level 5: “Hold” - the plane was put in this level manually

Then implement an `audit` method which examines the entire queue and reassigns all planes to their correct priority level based on these business rules. Order should be maintained within the level, so when an audit moves a plane from Level 3 to Level 1, it goes to the end of the Level 1 list.