
source_single_valued_parameters = (
    'type',
    'sql_host', 'sql_user', 'sql_pass', 'sql_db', 'sql_port',
    'sql_sock',

    'json_autoconv_numbers',
    'json_autoconv_keynames',
    'on_json_attr_error',

    'mysql_connect_flags',
    'mysql_ssl_cert', 'mysql_ssl_key', 'mysql_ssl_ca',

    'mssql_winauth', 'mssql_unicode',

    'odbc_dsn',

    'sql_column_buffers',

    'sql_query',
    'sql_joined_field',
    'sql_query_post',
    'sql_query_post_index',
    'sql_ranged_throttle',
    'sql_query_range',
    'sql_range_step',
    'sql_query_killlist',
    'sql_query_info',

    'unpack_zlib',
    'unpack_mysqlcompress',
    'unpack_mysqlcompress_maxsize'
)

source_multi_valued_parameters = (
    'sql_query_pre',

    'xmlpipe_attr_uint',
    'xmlpipe_attr_bigint',
    'xmlpipe_attr_bool',
    'xmlpipe_attr_timestamp',
    'xmlpipe_attr_str2ordinal',
    'xmlpipe_attr_float',
    'xmlpipe_attr_multi',
    'xmlpipe_attr_multi_64',
    'xmlpipe_attr_string',
    'xmlpipe_attr_wordcount',
    'xmlpipe_attr_json',
    'xmlpipe_fixup_utf8',

    'xmlpipe_command',
    'xmlpipe_field',
    'xmlpipe_field_string',
    'xmlpipe_field_wordcount',

    'sql_attr_uint',
    'sql_attr_timestamp',
    'sql_attr_float',
    'sql_attr_str2ordinal',
    'sql_attr_string',
    'sql_attr_json',
    'sql_attr_multi',
    'sql_attr_bool',
    'sql_attr_bigint',
    'sql_attr_str2wordcount',

    'sql_field_string',
    'sql_field_str2wordcount',
    'sql_file_field'
)

source_parameters = source_single_valued_parameters + source_multi_valued_parameters

source_mandatory_parameters = (
    'type',
    'sql_host',
    'sql_user',
    'sql_pass',
    'sql_db',
    'sql_query',
)

source_limited_options = {
    'type': ('mysql', 'pgsql', 'mssql', 'xmlpipe', 'xmlpipe2', 'odbc'),
}


index_single_valued_parameters = (
    'type',
    'source',
    'path',
    'docinfo',
    'mlock',
    'morphology',
    'dict',
    'index_sp',
    'index_zones',
    'min_stemming_len',
    'stopwords',
    'wordforms',
    'embedded_limit',
    'exceptions',
    'min_word_len',
    'charset_table',
    'ignore_chars',
    'min_prefix_len',
    'min_infix_len',
    'max_substring_len',
    'prefix_fields',
    'infix_fields',
    'enable_star',
    'ngram_len',
    'ngram_chars',
    'phrase_boundary',
    'phrase_boundary_step',
    'html_strip',
    'html_index_attrs',
    'html_remove_elements',
    'local',
    'agent',
    'agent_persistent',
    'agent_blackhole',
    'agent_connect_timeout',
    'agent_query_timeout',
    'preopen',
    'ondisk_dict',
    'inplace_enable',
    'inplace_hit_gap',
    'inplace_docinfo_gap',
    'inplace_reloc_factor',
    'inplace_write_factor',
    'index_exact_words',
    'overshort_step',
    'stopword_step',
    'hitless_words',
    'expand_keywords',
    'blend_chars',
    'blend_mode',
    'rt_mem_limit',
    'ha_strategy',
    'bigram_freq_words',
    'bigram_index',
    'index_field_lengths',
    'regexp_filter',
    'stopwords_unstemmed',
    'global_idf',
)

index_multi_valued_parameters = (
    'rt_field',
    'rt_attr_uint',
    'rt_attr_bool',
    'rt_attr_bigint',
    'rt_attr_float',
    'rt_attr_multi',
    'rt_attr_multi_64',
    'rt_attr_timestamp',
    'rt_attr_string',
    'rt_attr_json',
)

index_parameters = index_single_valued_parameters + index_multi_valued_parameters

index_mandatory_parameters = (
    'source',
    'path',
)

indexer_parameters = (
    'mem_limit',
    'max_iops',
    'max_iosize',
    'max_xmlpipe2_field',
    'write_buffer',
    'max_file_field_buffer',
    'on_file_field_error',
    'lemmatizer_base',
    'lemmatizer_cache',
)

searchd_parameters = (
    'listen',
    'log',
    'query_log',
    'query_log_format',
    'read_timeout',
    'client_timeout',
    'max_children',
    'pid_file',
    'max_matches',
    'seamless_rotate',
    'preopen_indexes',
    'unlink_old',
    'attr_flush_period',
    'ondisk_dict_default',
    'max_packet_size',
    'mva_updates_pool',
    'crash_log_path',
    'max_filters',
    'max_filter_values',
    'listen_backlog',
    'read_buffer',
    'read_unhinted',
    'max_batch_queries',
    'subtree_docs_cache',
    'subtree_hits_cache',
    'workers',
    'dist_threads',
    'binlog_path',
    'binlog_flush',
    'binlog_max_log_size',
    'snippets_file_prefix',
    'collation_server',
    'collation_libc_locale',
    'plugin_dir',
    'mysql_version_string',
    'rt_flush_period',
    'thread_stack',
    'expansion_limit',
    'compat_sphinxql_magics',
    'watchdog',
    'prefork_rotation_throttle',
    'sphinxql_state',
    'ha_ping_interval',
    'ha_period_karma',
    'persistent_connections_limit',
    'rt_merge_iops',
    'rt_merge_maxiosize',
    'predicted_time_costs',
)

searchd_mandatory_parameters = (
    'pid_file',
)

connection_parameters = (
    'host',
    'port'
)

connection_mandatory_parameters = ()

reserved_keywords = (
    'AND',
    'AGENT',
    'AS',
    'ASC',
    'AVG',
    'BEGIN',
    'BETWEEN',
    'BY',
    'CALL',
    'COLLATION',
    'COMMIT',
    'COUNT',
    'DELETE',
    'DESC',
    'DESCRIBE',
    'DISTINCT',
    'FALSE',
    'FROM',
    'GLOBAL',
    'GROUP',
    'ID',
    'IN',
    'INSERT',
    'INTO',
    'LIMIT',
    'MATCH',
    'MAX',
    'META',
    'MIN',
    'NOT',
    'NULL',
    'OPTION',
    'OR',
    'ORDER',
    'REPLACE',
    'ROLLBACK',
    'SELECT',
    'SET',
    'SHOW',
    'START',
    'STATUS',
    'SUM',
    'TABLES',
    'TRANSACTION',
    'TRUE',
    'UPDATE',
    'VALUES',
    'VARIABLES',
    'WARNINGS',
    'WEIGHT',
    'WHERE',
    'WITHIN',
)
