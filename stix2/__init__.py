"""Python APIs for STIX 2.

.. autosummary::
   :toctree: api

   core
   datastore
   environment
   exceptions
   markings
   patterns
   properties
   sources
   utils
   patterns
   properties
   utils
   workbench
   v20.common
   v20.observables
   v20.sdo
   v20.sro
   v21.common
   v21.observables
   v21.sdo
   v21.sro

   The .v21 import can't be relocated, or we get circular import problems.
   The 'isort:skip' line comment didn't work to skip only that one problematic
   import.  The only thing that did was telling it to skip the whole file.

   isort:skip_file
"""

# flake8: noqa

from .core import _collect_stix2_mappings, parse, parse_observable
from .v21 import *  # This import will always be the latest STIX 2.X version
from .datastore import CompositeDataSource
from .datastore.filesystem import (
    FileSystemSink, FileSystemSource,
    FileSystemStore
)
from .datastore.filters import Filter
from .datastore.memory import MemorySink, MemorySource, MemoryStore
from .datastore.taxii import (
    TAXIICollectionSink, TAXIICollectionSource,
    TAXIICollectionStore
)
from .environment import Environment, ObjectFactory
from .markings import (
    add_markings, clear_markings, get_markings, is_marked,
    remove_markings, set_markings
)
from .patterns import (
    AndBooleanExpression, AndObservationExpression,
    BasicObjectPathComponent, BinaryConstant,
    BooleanConstant, EqualityComparisonExpression,
    FloatConstant, FollowedByObservationExpression,
    GreaterThanComparisonExpression,
    GreaterThanEqualComparisonExpression, HashConstant,
    HexConstant, InComparisonExpression, IntegerConstant,
    IsSubsetComparisonExpression,
    IsSupersetComparisonExpression,
    LessThanComparisonExpression,
    LessThanEqualComparisonExpression,
    LikeComparisonExpression, ListConstant,
    ListObjectPathComponent, MatchesComparisonExpression,
    ObjectPath, ObservationExpression, OrBooleanExpression,
    OrObservationExpression, ParentheticalExpression,
    QualifiedObservationExpression,
    ReferenceObjectPathComponent, RepeatQualifier,
    StartStopQualifier, StringConstant, TimestampConstant,
    WithinQualifier
)
from .utils import new_version, revoke
from .version import __version__

from .STIXPatternVisitor import create_pattern_object

_collect_stix2_mappings()

DEFAULT_VERSION = '2.1'  # Default version will always be the latest STIX 2.X version
