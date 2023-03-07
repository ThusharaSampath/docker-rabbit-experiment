# ------------------------------------------------------------------------
#
# Copyright 2022 WSO2, LLC. (http://wso2.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License
#
# ------------------------------------------------------------------------

# set base Docker image to Alpine Docker image
FROM wso2/wso2mi:latest


ARG USER=wso2mi
ARG USER_ID=10001
ARG USER_GROUP=wso2mi
ARG USER_GROUP_ID=10001
ARG USER_HOME=/home/${USER}

USER root
RUN \
    addgroup --system -g ${USER_GROUP_ID} ${USER_GROUP} \
    && adduser --system --home ${USER_HOME} -g ${USER_GROUP_ID} -u ${USER_ID} ${USER}

RUN chown -R ${USER_GROUP}:${USER} "${WORKING_DIRECTORY}"/

USER 10001
RUN chmod +x "${WORKING_DIRECTORY}"/docker-entrypoint.sh

COPY ./sales-rabbitmq-inboundCompositeExporter_1.0.0-SNAPSHOT.car "${WSO2_SERVER_HOME}/repository/deployment/server/carbonapps/"

ENTRYPOINT ["/home/wso2carbon/docker-entrypoint.sh"]