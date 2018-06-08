from __future__ import absolute_import, division, print_function, unicode_literals

import gutter.client.settings
import gutter.django
from durabledict.redis import RedisDict
from gutter.client.default import gutter as manager
from gutter.client.models import Condition, Switch
from gutter.client.operators.comparable import Equals, MoreThan
from gutter.client.operators.misc import Percent
from redis import Redis

from .arguments import Request, User

# Configure Gutter
gutter.client.settings.manager.storage_engine = RedisDict('gutter', Redis())


switch = Switch('cool_feature', label='A cool feature', description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

condition = Condition(User, 'name', Equals(value='Jeff'))
switch.conditions.append(condition)

condition = Condition(User, 'age', MoreThan(lower_limit=21))
switch.conditions.append(condition)

manager.register(switch)

switch = Switch('other_neat_feature', label='A neat additional feature', description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

condition = Condition(Request, 'ip', Percent(percentage=10))
switch.conditions.append(condition)

manager.register(switch)

for switch in manager.switches:
    print('+', switch)

print(type(manager.storage))
