### Groups with Groups and Children ###

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == None or group == None:
        return False
    
    # print(f'grpup get users {group.get_users()}')
    if user in group.get_users():
        # print(f'u {u} user {user}')
        # if u == user:
        return True
            
    # print(f'grpup get grups {group.get_groups()}')
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True 
        
    return False

# Test Group Class
print('Test 1: Test Group Class')
parent = Group("parent")
print(f'Group parent should have name: parent Result: {parent.get_name()}')
assert('parent' == parent.get_name())

parent.add_user('android')
print(f'Group parent should have one child called:  android Result: {parent.get_users()}')
assert(['android'] == parent.get_users())

parent.add_group('humanoids')
print(f'Group parent should have one group called:  humanoids Result: {parent.get_groups()}')
assert(['humanoids'] == parent.get_groups())

# Test case 2 -  In Group
print('Test 2: Test Child in Group')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print(f'should return True - Result: {is_user_in_group(sub_child_user, parent)}')
assert(True == is_user_in_group(sub_child_user, parent))

# Test case 3 - Not In Group
print('Test 3: Test Not In Group')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

sub_child_user_not = 'sub_not_in_group'

print(f'should return False - Result: {is_user_in_group(sub_child_user_not, parent)}')
assert(False == is_user_in_group(sub_child_user_not, parent))

# Test 4 - None child provided to is_user_in_group()
print('Test 4 - None child provided is_user_in_group()')
parent = Group("parent")
child_user = "sub_child_user"
parent.add_user(child_user)
print(f'should return False - Result: {is_user_in_group(None, parent)}')
assert(False == is_user_in_group(None, parent))
