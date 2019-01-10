from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:
    """
    - create a `defaultdict` object, and its default value would be set to the string `Unknown`.
    - Add an entry with key name `Alan` and its value being `Manchester`.
    - Return the `defaultdict` object you created.
    """
    # you code starts here:
    d = defaultdict(lambda: "Unknown")
    d["Alan"] = "Manchester"
    return d


def task2(arg_od: OrderedDict):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """
    # you code starts here:
    arg_od.popitem(False)
    arg_od.popitem(True)
    arg_od.move_to_end("Bob", True)
    arg_od.move_to_end("Dan", False)


Person = namedtuple("Player", "name club")


def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    # you code starts here:

    player = Person(name, club)
    return player


def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    # you code starts here:
    arg_deque.pop()
    arg_deque.append(arg_deque.popleft())
    arg_deque.appendleft('Zack')


dd = task1()
print(dd)

player = task3("Reynaldo", "Juventus")
print(player)

dq = deque()
dq.append("George")
dq.append("Cheri")
dq.append("Jax")
print(dq)
task4(dq)
print(dq)
