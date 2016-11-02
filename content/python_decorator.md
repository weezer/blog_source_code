Title: Python Decorator example by openstack Horizon source code
Date: 2016-09-19 22:07
Category: tech
Tags: tricks, python,
Slug: python-decorator-by-openstack-horizon
Authors: Weezer Su
Summary: Openstack Horizon coders like to use alot of tricks in the project.

Below is a example from the horizon integration testing script.
```python
def bind_table_action(action_name):
    _actions_locator = (by.By.CSS_SELECTOR, 'div.table_actions > button,'
                                            ' div.table_actions > a')

    def decorator(method):
        @functools.wraps(method)
        def wrapper(table):
            actions = table._get_elements(*_actions_locator)
            action_element = None
            for action in actions:
                target_action_id = '%s__action_%s' % (table.name, action_name)
                if action.get_attribute('id') == target_action_id:
                    action_element = action
                    break
            if action_element is None:
                msg = "Could not bind method '%s' to action control '%s'" % (
                    method.__name__, action_name)
                raise ValueError(msg)
            return method(table, action_element)
        return wrapper
    return decorator
```

how to use it? you can see it's a **DECORATOR**, so if you have any funtion or method you can decorate it with the above script for make it as another one. the real function you get will be the one **return method(table, action_element)**.

but what the fuck is the return method(table, action_element)? the first layer is useless, just give the action_name to the error message, second layer is the real decorator, @functools.wraps just fetch the docs from the method you put into the parameter, and the damn **'table'**, actually it's the first argument from the method you just passed into decorator and functools.wraps. BE AWARE! if you are decorating a class method, the first argument is **'self'**, the instance itself!!!!
