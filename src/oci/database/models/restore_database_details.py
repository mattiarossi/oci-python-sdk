# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class RestoreDatabaseDetails(object):

    def __init__(self):

        self.swagger_types = {
            'database_scn': 'str',
            'latest': 'bool',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'database_scn': 'databaseSCN',
            'latest': 'latest',
            'timestamp': 'timestamp'
        }

        self._database_scn = None
        self._latest = None
        self._timestamp = None

    @property
    def database_scn(self):
        """
        Gets the database_scn of this RestoreDatabaseDetails.
        Restores using the backup with the System Change Number (SCN) specified.


        :return: The database_scn of this RestoreDatabaseDetails.
        :rtype: str
        """
        return self._database_scn

    @database_scn.setter
    def database_scn(self, database_scn):
        """
        Sets the database_scn of this RestoreDatabaseDetails.
        Restores using the backup with the System Change Number (SCN) specified.


        :param database_scn: The database_scn of this RestoreDatabaseDetails.
        :type: str
        """
        self._database_scn = database_scn

    @property
    def latest(self):
        """
        Gets the latest of this RestoreDatabaseDetails.
        Restores to the last known good state with the least possible data loss.


        :return: The latest of this RestoreDatabaseDetails.
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """
        Sets the latest of this RestoreDatabaseDetails.
        Restores to the last known good state with the least possible data loss.


        :param latest: The latest of this RestoreDatabaseDetails.
        :type: bool
        """
        self._latest = latest

    @property
    def timestamp(self):
        """
        Gets the timestamp of this RestoreDatabaseDetails.
        Restores to the timestamp specified.


        :return: The timestamp of this RestoreDatabaseDetails.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this RestoreDatabaseDetails.
        Restores to the timestamp specified.


        :param timestamp: The timestamp of this RestoreDatabaseDetails.
        :type: datetime
        """
        self._timestamp = timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
