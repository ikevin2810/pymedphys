# Copyright (C) 2019 South Western Sydney Local Health District,
# University of New South Wales

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""A tool to export DICOM objects from raw Pinnacle data:

.. WARNING::
   The DICOM objects exported by this tool are not the same as the DICOM
   objects exported from within the Pinnacle application. Certain DICOM
   modalities correspond fairly well to the Pinnacle exported objects
   for some versions of Pinnacle. Others are not working as expected or
   have not been validated.

   The first step when using this tool is to compare the output generated
   to the 'ground truth' generated by your version(s) of Pinnacle. You can
   then determine if this tool currently meets your export needs, or if
   some adjustments need to be made. Please create an issue on the PyMedPhys
   GitHub describing the circumstances where the tool is not working,
   providing some sample raw Pinnacle data where possible. If you're up for
   a challenge, clone the PyMedPhys repository and attempt to solve the
   problem yourself! Don't be afraid to ask for help when contributing your
   changes. The more developers we can encourage to contribute to this tool,
   the sooner it will become stable and reliable.

   Finally, note that while this tool can be extremely useful for exporting
   large amounts of Pinnacle data to DICOM, we recommend that this should
   only be used for research purposes and not clinically.
"""

# pylint: disable = unused-import

from pymedphys._experimental.pinnacle import PinnacleExport, PinnacleImage, PinnaclePlan
