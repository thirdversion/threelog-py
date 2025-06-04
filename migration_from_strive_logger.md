# Migration Guide from Strive Logger to Three Log

An alias is available for the ThreeLog class to make it easier to migrate from Strive Logger. If you are switching from Strive Logger, you only need to update all imports which reference the strivelogger package to reference threelog instead, and then you can use the StriveLogger alias for the ThreeLog class as a drop-in replacement.

Current code using Strive Logger:

```python

from strivelogger import StriveLogger
StriveLogger.initialize(logger=ConsoleLogger())
StriveLogger.info("This is an info message")
```

Updated code using Three Log:

```python
from threelog import StriveLogger
StriveLogger.initialize(logger=ConsoleLogger())
StriveLogger.info("This is an info message")
```

The StriveLogger alias will continue to work as a drop-in replacement for the ThreeLog class, so you can continue to use it in your code without any changes. However, we recommend using the ThreeLog class directly in new code, as it is the official name of the package and compability may not be guaranteed in the future.
