#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cmk.gui.i18n import _

# Import the data structures the GUI uses to pass defaults:

from cmk.gui.valuespec import (
    Dictionary,
    Tuple,
    Float,
    TextAscii,
    ListOf,
    ValueSpec,
    TextInput
)
from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersOperatingSystem,
)


def _parameter_valuespec_jolokia_generic_levels():
    return Dictionary(
        elements=[
            ("levels",
                ListOf (
                    Tuple(
                        title=_("Levels"),
                        elements=[
                            Float(title=_("Warning if below"), default_value=-1.0),
                            Float(title=_("Critical if below"), default_value=-1.0),
                            Float(title=_("Warning if above"), default_value=0.0),
                            Float(title=_("Critical if above"), default_value=0.0),
                            TextAscii(
                                title=_("Name of the MBean/Attribute (optional)"),
                                help=_(
                                    "This might be helpful if you group some values together and want the Threshold only on a particular value.")
                            ),
                        ],
                    )
                )
            ),
        ],
        optional_keys=["levels", "expectedStrings"]
        # required_keys=['levels'],  # There is only one value, so its required
    )

def _item_spec() -> ValueSpec:
    return TextAscii(
            title = _("Item Name"),
            help = _("Name of the Service description without the JVM prefix")
        )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        # as defined in your check in share/check_mk/checks/
        check_group_name = "jvm_generic",
        group = RulespecGroupCheckParametersOperatingSystem,
        match_type = "dict",
        # the function above to issue default parameters
        parameter_valuespec = _parameter_valuespec_jolokia_generic_levels,
        title=lambda: _("Levels for the Metrics"),
        item_spec=_item_spec,
    )
)