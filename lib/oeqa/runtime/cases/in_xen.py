#
# SPDX-License-Identifier: MIT
#

from oeqa.runtime.case import OERuntimeTestCase
from oeqa.core.decorator.depends import OETestDepends

class InXenTest(OERuntimeTestCase):
    """
    Very basic test to verify that the /proc/xen device nodes are present.
    """

    @OETestDepends(['ssh.SSHTest.test_ssh'])
    def test_in_xen(self):
        (status, output) = self.target.run("test -d /proc/xen")
        self.assertEqual(status, 0, "Xen device nodes not present")
