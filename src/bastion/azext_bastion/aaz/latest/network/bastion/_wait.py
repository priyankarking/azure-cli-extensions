# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network bastion wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/bastionhosts/{}", "2024-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.bastion_host_name = AAZStrArg(
            options=["-n", "--name", "--bastion-host-name"],
            help="The name of the Bastion Host.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Resource group name of the Bastion Host.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BastionHostsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class BastionHostsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts/{bastionHostName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "bastionHostName", self.ctx.args.bastion_host_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType()
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.zones = AAZListType()

            properties = cls._schema_on_200.properties
            properties.disable_copy_paste = AAZBoolType(
                serialized_name="disableCopyPaste",
            )
            properties.dns_name = AAZStrType(
                serialized_name="dnsName",
            )
            properties.enable_file_copy = AAZBoolType(
                serialized_name="enableFileCopy",
            )
            properties.enable_ip_connect = AAZBoolType(
                serialized_name="enableIpConnect",
            )
            properties.enable_kerberos = AAZBoolType(
                serialized_name="enableKerberos",
            )
            properties.enable_session_recording = AAZBoolType(
                serialized_name="enableSessionRecording",
            )
            properties.enable_shareable_link = AAZBoolType(
                serialized_name="enableShareableLink",
            )
            properties.enable_tunneling = AAZBoolType(
                serialized_name="enableTunneling",
            )
            properties.ip_configurations = AAZListType(
                serialized_name="ipConfigurations",
            )
            properties.network_acls = AAZObjectType(
                serialized_name="networkAcls",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.scale_units = AAZIntType(
                serialized_name="scaleUnits",
            )
            properties.virtual_network = AAZObjectType(
                serialized_name="virtualNetwork",
            )
            _WaitHelper._build_schema_sub_resource_read(properties.virtual_network)

            ip_configurations = cls._schema_on_200.properties.ip_configurations
            ip_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.ip_configurations.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.ip_configurations.Element.properties
            properties.private_ip_allocation_method = AAZStrType(
                serialized_name="privateIPAllocationMethod",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_address = AAZObjectType(
                serialized_name="publicIPAddress",
                flags={"required": True},
            )
            _WaitHelper._build_schema_sub_resource_read(properties.public_ip_address)
            properties.subnet = AAZObjectType(
                flags={"required": True},
            )
            _WaitHelper._build_schema_sub_resource_read(properties.subnet)

            network_acls = cls._schema_on_200.properties.network_acls
            network_acls.ip_rules = AAZListType(
                serialized_name="ipRules",
            )

            ip_rules = cls._schema_on_200.properties.network_acls.ip_rules
            ip_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_acls.ip_rules.Element
            _element.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )

            sku = cls._schema_on_200.sku
            sku.name = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Wait"]
