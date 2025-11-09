def create_stack():  # create stack
    return []  # create stack using list


def is_empty(stack):  # check is empty
    return len(stack) == 0  # True is empty, False is full


def push(stack: list, item):  # add element in end(up) of stack
    stack.append(item)


def pop(stack: list):  # return element end(up) if stack and delete
    if not is_empty(stack):
        return stack.pop()
    else:
        return None


def peak(stack: list):  # return last element of stack
    if not is_empty(stack):
        return stack[-1]
    else:
        return None


if __name__ == "__main__":
    mystack = create_stack()
    print("Stack create", mystack)  # []
    push(mystack, 1)
    print("Stack after push", mystack)  # [1]
    push(mystack, 2)
    print("Stack after push", mystack)  # [1, 2]
    push(mystack, 3)
    print("Stack after all push", mystack)  # [1, 2, 3]
    print("Return last element of stack", peak(mystack))  # 3
    print("Stack after peak", mystack)  # [1, 2, 3]
    print("Deleted last element using pop", pop(mystack))  # 3
    print("Stack after pop", mystack)  # [1, 2]
