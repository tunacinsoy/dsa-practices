"""

Description:
  I thought that the list would be good for stack implementation, then i realized that dictionary could also suffice.

  transaction_stack will be used to store the original value of keys, meaning that if an operation happens, within a transaction,
  db would get the new value, however, its original value will be stored in transaction_stack, and in case of rollback situation,
  we would need to retrieve the elements from there.

  Because of this approach, the commit function becomes super clear, since we do not need to do anything else, than clearing the transaction_stack,
  since all original values are updated.


Test Cases:

    set a 10
    begin
    set a 20
    begin
    set a 30
    rollback
    get a -> 20

    transaction_stack[-1] = {
        a: 10

    }

    db =  {
            "a":10

          }



Complexities:
  Time:
  Space:
"""


class Solution:
    def __init__(self):
        # The actual in memory db itself
        self.db = {}
        # Will be used as stack to store transactions
        self.transaction_stack = []

    def set(self, key: str, val: int) -> None:

        if self.transaction_stack:
            # Record the value only if it's not already recorded
            if key not in self.transaction_stack[-1]:
                # Within this, my stack's dictionary will hold the key's value, if does not exist it return None
                self.transaction_stack[-1][key] = self.db.get(key, None)

        # We only need to insert the val of key to dictionary
        # only if transaction stack is empty, meaning that
        # we are not in a transaction block
        self.db[key] = val

    def get(self, key: str):
        if key in self.db:
            # print(self.db[key])
            return self.db[key]
        else:
            # print("NULL")
            return None

    def delete(self, key: str) -> None:

        # Key exists in the db
        if key in self.db:
            # We should check for if we are in a transaction session
            if self.transaction_stack:
                # If the topmost element in stack, then we are getting it
                # from the db
                if key not in self.transaction_stack[-1]:
                    self.transaction_stack[-1][key] = self.db[key]
            del self.db[key]

        # Key is not in the db, but we might still be in transaction block
        else:
            # If there is a transaction going on
            if self.transaction_stack:
                # Let's record the deletion of a non-existent key
                if key not in self.transaction_stack[-1]:
                    self.transaction_stack[-1][key] = None

    def count(self, val: int) -> int:
        cnt = list(self.db.values()).count(val)
        # print(cnt)
        return cnt

    def begin(self):
        # adding an empty dictionary in our stack
        # to start a new transaction
        self.transaction_stack.append({})

    def rollback(self):
        if not self.transaction_stack:
            print("NO TRANSACTION")

        else:
            # Pop the changes from the stack

            # Changes that have applied within a transaction block are popped
            changes = self.transaction_stack.pop()
            for key, original_value in changes.items():

                # Means that this key has never existed before
                if original_value is None:
                    # Delete the keys that did not exist before
                    self.db.pop(key, None)
                else:
                    self.db[key] = original_value

    def commit(self):
        if not self.transaction_stack:
            print("NO TRANSACTION")

        else:
            # I have committed everything, so there's no need to consider transaction_stack
            # We can just dump it
            self.transaction_stack.clear()


def test_solution():

    solution = Solution()

    # Test SET
    solution.set("x", 10)
    solution.set("y", 10)
    solution.set("z", 30)

    # Test COUNT
    assert solution.count(10) == 2

    # Test GET
    assert solution.get("x") == 10
    assert solution.get("b") == None

    # Test DELETE
    solution.delete("x")
    assert solution.get("x") == None

    # # Test Transactions with new keys
    # solution.begin()
    # solution.set("b", 40)  # New key within transaction
    # assert solution.get("b") == 40
    # solution.begin()
    # solution.set("c", 50)  # Another new key
    # assert solution.get("c") == 50

    # # Rollback most recent transaction
    # solution.rollback()
    # assert solution.get("c") is None  # 'c' should be removed
    # assert solution.get("b") == 40  # 'b' should still exist

    # # Rollback again
    # solution.rollback()
    # assert solution.get("b") is None  # 'b' should be removed

    # # Attempt to rollback with no transactions
    # solution.rollback()  # Should print "NO TRANSACTION"

    # # Test COMMIT with new keys
    # solution.begin()
    # solution.set("d", 60)
    # print(solution.get("d"))
    # solution.set("e", 70)
    # solution.commit()
    # assert solution.get("d") == 60
    # assert solution.get("e") == 70

    # # Attempting to rollback after commit
    # solution.rollback()  # Should print "NO TRANSACTION"

    # set a 10
    # begin
    # set a 20
    # begin
    # set a 30
    # rollback
    # get a -> 20

    solution.set("a", 10)
    solution.begin()
    solution.set("a", 20)
    solution.begin()
    solution.set("b", 10)
    solution.begin()
    solution.set("a", 30)
    solution.rollback()
    print(solution.get("a"))
    print(solution.get("b"))


test_solution()
print("All tests passed!")
