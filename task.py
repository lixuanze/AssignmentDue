class Task:

    __slots__ = 'group', 'content', 'due_date', 'stakeholders'

    def __init__(self, group, content, due_date=None, stakeholders=[]):
        self.group = group
        self.content = content
        self.due_date = due_date
        self.stakeholders = stakeholders

    def add_dependency(self, user1, user2):
        '''(Task, User, User) -> None'''
        index1, index2 = -1, -1
        for i in range(len(self.stakeholders)):
            if user1 in self.stakeholders[i]:
                index1 = i
                break
        for i in range(len(self.stakeholders)):
            if user2 in self.stakeholders[i]:
                index2 = i
                break
        if index1 >= 0 and index2 >= 0:
            # both users exists in the task
            if index1 == index2:
                # already in the same set
                pass
            else:
                # merge two sets
                self.stakeholders[index1] = \
                    self.stakeholders[index1].union(self.stakeholders[index2])
                del self.stakeholders[index2]
        elif index1 >= 0:
            # user1 in the task but user2 does not
            self.stakeholders[index1].add[user2]
        elif index2 >= 0:
            # user2 in the task but user1 does not
            self.stakeholders[index2].add[user1]
        else:
            # neither user is in the task
            self.stakeholders.append({user1, user2})

    def finish_task(self, user):
        '''(Task, User) -> None'''
        index = -1
        for i in range(self.stakeholders):
            if user in self.stakeholders[i]:
                index = i
                break
        if index < 0:
            raise Exception('User should not have access of the task')
        del self.stakeholders[index]