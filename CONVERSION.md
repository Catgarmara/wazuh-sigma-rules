# Conversion record

Every custom rule live on the source Wazuh 4.14 manager on 2026-10-12, and where it went.

| Status | Count | Meaning |
|---|---|---|
| converted | 440 | Converted. Twins on the two access-log streams with an identical pattern share one file. |
| merged | 14 | Twin whose regex or status gate differed. Folded into the kept variant (README, Intentional changes). |
| hand | 5 | Converted by hand (constructs the drafter does not map). |
| filter | 8 | Became a Sigma filter on the rule it tuned. |
| not converted | 49 | See the reason column. |
| **total** | **516** | |

## Rules

| Wazuh ID | Wazuh level | Status | Sigma file | Reason |
|---|---|---|---|---|
| 31161 | 6 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 31163 | 6 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100001 | 5 | not converted |  | Stock Wazuh example rule. |
| 100100 | 6 | converted | `rules/web/sql-injection/sql_injection_union_select_or_select_from_where_pattern_detected_in_ur.yml` |  |
| 100101 | 6 | merged | `rules/web/sql-injection/sql_injection_or_based_injection_attempt_via_encoded_characters.yml` |  |
| 100102 | 8 | converted | `rules/web/sql-injection/sql_injection_stored_procedure_execution_attempt_sp_xp.yml` |  |
| 100103 | 8 | converted | `rules/web/sql-injection/sql_injection_destructive_ddl_statement_detected_drop_truncate_alter_t.yml` |  |
| 100104 | 6 | converted | `rules/web/sql-injection/sql_injection_database_metadata_enumeration_attempt.yml` |  |
| 100105 | 6 | converted | `rules/web/sql-injection/sql_injection_time_based_blind_injection_attempt_sleep_benchmark_waitf.yml` |  |
| 100106 | 7 | converted | `rules/web/sql-injection/sql_injection_file_read_write_attempt_via_sql_load_file_into_outfile.yml` |  |
| 100107 | 10 | converted | `rules/web/sql-injection/sql_injection_error_based_injection_via_having_group_by_with_aggregate.yml` |  |
| 100108 | 6 | converted | `rules/web/sql-injection/sql_injection_sql_comment_terminator_detected_at_end_of_parameter.yml` |  |
| 100109 | 12 | converted | `rules/correlations/sql_injection_repeated_sqli_attempts.yml` |  |
| 100110 | 7 | converted | `rules/web/sql-injection/sql_injection_cast_convert_type_coercion_detected_in_url.yml` |  |
| 100111 | 7 | converted | `rules/web/sql-injection/sql_injection_string_function_abuse_detected_char_concat_group_concat.yml` |  |
| 100120 | 6 | converted | `rules/web/xss/xss_script_tag_detected_in_url_parameter.yml` |  |
| 100121 | 6 | converted | `rules/web/xss/xss_event_handler_injection_attempt.yml` |  |
| 100122 | 6 | converted | `rules/web/xss/xss_javascript_or_vbscript_uri_scheme_injection_attempt.yml` |  |
| 100123 | 7 | converted | `rules/web/xss/xss_embedded_content_tag_injection.yml` |  |
| 100124 | 6 | converted | `rules/web/xss/xss_tag_with_event_handler_injection.yml` |  |
| 100125 | 6 | converted | `rules/web/xss/xss_dom_based_xss_object_access_in_url.yml` |  |
| 100126 | 6 | converted | `rules/web/xss/xss_javascript_function_injection.yml` |  |
| 100127 | 7 | converted | `rules/web/xss/xss_css_based_injection_attempt.yml` |  |
| 100128 | 12 | converted | `rules/correlations/xss_repeated_xss_attempts_from_same_source.yml` |  |
| 100129 | 6 | converted | `rules/web/xss/xss_data_uri_with_html_content_type_detected.yml` |  |
| 100140 | 8 | converted | `rules/web/rfi-lfi/rfi_remote_file_inclusion_attempt_via_url_parameter_with_protocol_sche.yml` |  |
| 100141 | 7 | converted | `rules/web/rfi-lfi/rfi_php_stream_wrapper_abuse_php_filter_php_input_php_data.yml` |  |
| 100142 | 7 | converted | `rules/web/rfi-lfi/rfi_exotic_php_wrapper_detected_expect_zip_phar_glob.yml` |  |
| 100143 | 7 | converted | `rules/web/rfi-lfi/lfi_deep_directory_traversal_attempt_3_levels.yml` |  |
| 100144 | 8 | converted | `rules/web/rfi-lfi/lfi_attempted_access_to_sensitive_unix_system_files.yml` |  |
| 100145 | 8 | converted | `rules/web/rfi-lfi/lfi_proc_self_access_attempt.yml` |  |
| 100146 | 7 | converted | `rules/web/rfi-lfi/lfi_windows_system_file_access_attempt.yml` |  |
| 100147 | 7 | converted | `rules/web/rfi-lfi/lfi_sensitive_configuration_file_access_attempt.yml` |  |
| 100148 | 7 | converted | `rules/web/rfi-lfi/lfi_log_file_inclusion_attempt.yml` |  |
| 100149 | 12 | converted | `rules/correlations/file_inclusion_repeated_rfi_lfi_attempts.yml` |  |
| 100160 | 8 | converted | `rules/web/command-injection/command_injection_pipe_to_recon_command_detected_in_url.yml` |  |
| 100161 | 8 | converted | `rules/web/command-injection/command_injection_semicolon_chained_command_detected_in_url.yml` |  |
| 100162 | 8 | converted | `rules/web/command-injection/command_injection_backtick_or_command_substitution_detected.yml` |  |
| 100163 | 9 | converted | `rules/web/command-injection/command_injection_remote_file_download_attempt_via_wget_curl.yml` |  |
| 100164 | 10 | converted | `rules/web/command-injection/command_injection_reverse_shell_attempt_via_netcat_socat.yml` |  |
| 100165 | 10 | converted | `rules/web/command-injection/command_injection_bash_reverse_shell_pattern_detected.yml` |  |
| 100166 | 8 | converted | `rules/web/command-injection/command_injection_scripting_language_one_liner_execution_attempt.yml` |  |
| 100167 | 8 | converted | `rules/web/command-injection/command_injection_and_chained_command_detected.yml` |  |
| 100168 | 9 | converted | `rules/web/command-injection/command_injection_file_permission_change_attempt_chmod_chown.yml` |  |
| 100169 | 12 | converted | `rules/correlations/command_injection_repeated_os_command_injection_attempts_detected.yml` |  |
| 100180 | 6 | converted | `rules/web/path-traversal/path_traversal_basic_or_pattern_in_url.yml` |  |
| 100181 | 7 | converted | `rules/web/path-traversal/path_traversal_utf_8_overlong_encoding_bypass_attempt.yml` |  |
| 100182 | 7 | converted | `rules/web/path-traversal/path_traversal_double_url_encoding_bypass_attempt.yml` |  |
| 100183 | 7 | converted | `rules/web/path-traversal/path_traversal_hex_encoding_bypass_attempt.yml` |  |
| 100184 | 8 | converted | `rules/web/path-traversal/path_traversal_deep_traversal_4_levels.yml` |  |
| 100185 | 7 | converted | `rules/web/path-traversal/path_traversal_traversal_targeting_config_backup_key_files.yml` |  |
| 100186 | 12 | converted | `rules/correlations/path_traversal_repeated_traversal_attempts.yml` |  |
| 100200 | 8 | merged | `rules/web/xxe/xxe_doctype_entity_declaration_detected_in_request.yml` |  |
| 100201 | 9 | converted | `rules/web/xxe/xxe_system_entity_with_external_uri.yml` |  |
| 100202 | 8 | converted | `rules/web/xxe/xxe_public_entity_with_external_dtd_reference_detected.yml` |  |
| 100203 | 9 | converted | `rules/web/xxe/xxe_parameter_entity_declaration.yml` |  |
| 100204 | 8 | merged | `rules/web/xxe/xxe_xml_declaration_followed_by_doctype.yml` |  |
| 100205 | 9 | converted | `rules/web/xxe/xxe_entity_referencing_etc_passwd_or_file.yml` |  |
| 100206 | 10 | converted | `rules/web/xxe/xxe_entity_with_command_execution_or_php_filter_wrapper.yml` |  |
| 100207 | 12 | converted | `rules/correlations/xxe_repeated_xxe_injection_attempts_detected.yml` |  |
| 100220 | 8 | converted | `rules/web/ssrf/ssrf_request_to_localhost_loopback_via_url_parameter.yml` |  |
| 100221 | 8 | converted | `rules/web/ssrf/ssrf_request_targeting_internal_rfc1918_address_range.yml` |  |
| 100222 | 9 | converted | `rules/web/ssrf/ssrf_cloud_metadata_endpoint_169_254_169_254_access_attempt.yml` |  |
| 100223 | 8 | converted | `rules/web/ssrf/ssrf_ipv6_loopback_address_1_access_attempt.yml` |  |
| 100224 | 8 | converted | `rules/web/ssrf/ssrf_exotic_protocol_scheme_gopher_dict_ldap_tftp.yml` |  |
| 100225 | 8 | converted | `rules/web/ssrf/ssrf_url_with_embedded_credentials.yml` |  |
| 100226 | 8 | converted | `rules/web/ssrf/ssrf_obfuscated_localhost_via_decimal_octal_hex_ip_representation.yml` |  |
| 100227 | 9 | converted | `rules/web/ssrf/ssrf_cloud_instance_metadata_path_detected_aws_gcp_azure.yml` |  |
| 100228 | 12 | converted | `rules/correlations/ssrf_repeated_ssrf_attempts_detected.yml` |  |
| 100240 | 6 | not converted |  | Never matches in Wazuh: tests for a missing Referer header on a field the JSON access-log stream does not have; access logs carry no request headers. |
| 100241 | 7 | hand | `rules/web/csrf/csrf_post_to_sensitive_api_endpoint.yml` |  |
| 100242 | 8 | converted | `rules/web/csrf/csrf_successful_access_to_account_management_endpoint.yml` |  |
| 100243 | 12 | not converted |  | Correlation over 100240, which never matches. |
| 100250 | 8 | converted | `rules/web/http-smuggling/http_smuggling_both_transfer_encoding_and_content_length_headers.yml` |  |
| 100251 | 8 | converted | `rules/web/http-smuggling/http_smuggling_obfuscated_transfer_encoding_header_value.yml` |  |
| 100252 | 7 | converted | `rules/web/http-smuggling/http_smuggling_embedded_http_request_detected_within_body.yml` |  |
| 100253 | 7 | converted | `rules/web/http-smuggling/http_smuggling_duplicate_content_length_headers_detected.yml` |  |
| 100254 | 12 | converted | `rules/correlations/http_smuggling_repeated_smuggling_attempts.yml` |  |
| 100270 | 6 | converted | `rules/web/brute-force-web/web_brute_force_failed_login_attempt_401_403_on_auth_endpoint.yml` |  |
| 100271 | 10 | converted | `rules/correlations/web_brute_force_10_failed_logins_in_30s_from_same_ip.yml` |  |
| 100272 | 12 | converted | `rules/correlations/web_brute_force_30_failed_logins_in_60s.yml` |  |
| 100273 | 10 | converted | `rules/correlations/web_brute_force_failed_logins_from_multiple_ips.yml` |  |
| 100274 | 8 | converted | `rules/web/brute-force-web/web_brute_force_failed_cms_admin_login_attempt_wordpress_joomla.yml` |  |
| 100275 | 12 | converted | `rules/correlations/web_brute_force_repeated_cms_admin_login_failures.yml` |  |
| 100276 | 6 | merged | `rules/web/brute-force-web/web_brute_force_failed_api_authentication_attempt.yml` |  |
| 100277 | 10 | converted | `rules/correlations/web_brute_force_api_token_auth_brute_force.yml` |  |
| 100290 | 10 | converted | `rules/web/web-shell/web_shell_known_web_shell_filename_detected_in_url.yml` |  |
| 100291 | 9 | converted | `rules/web/web-shell/web_shell_command_parameter_pattern_detected.yml` |  |
| 100292 | 10 | converted | `rules/web/web-shell/web_shell_php_shell_code_pattern_eval_system_with_superglobal.yml` |  |
| 100293 | 9 | converted | `rules/web/web-shell/web_shell_php_dangerous_function_call_detected_in_url.yml` |  |
| 100294 | 10 | hand | `rules/web/web-shell/server_script_created_by_web_server_user.yml` |  |
| 100295 | 10 | converted | `rules/web/web-shell/web_shell_obfuscation_function_detected.yml` |  |
| 100296 | 9 | converted | `rules/web/web-shell/web_shell_server_side_script_accessed_from_upload_images_directory.yml` |  |
| 100297 | 9 | converted | `rules/web/web-shell/web_shell_double_extension_detected.yml` |  |
| 100298 | 14 | converted | `rules/correlations/web_shell_multiple_web_shell_indicators.yml` |  |
| 100310 | 6 | converted | `rules/web/api-abuse/api_abuse_rate_limit_triggered_http.yml` |  |
| 100311 | 10 | converted | `rules/correlations/api_abuse_persistent_rate_limit_violations.yml` |  |
| 100312 | 8 | merged | `rules/web/api-abuse/api_abuse_access_to_administrative_or_internal_api_endpoint.yml` |  |
| 100313 | 7 | merged | `rules/web/api-abuse/api_abuse_sequential_id_enumeration_on_api.yml` |  |
| 100314 | 10 | converted | `rules/correlations/api_abuse_rapid_sequential_id_enumeration.yml` |  |
| 100315 | 6 | merged | `rules/web/api-abuse/api_abuse_server_error_on_api_endpoint.yml` |  |
| 100316 | 10 | converted | `rules/correlations/api_abuse_many_server_errors_from_same_ip.yml` |  |
| 100330 | 7 | converted | `rules/web/http-response-splitting/http_response_splitting_crlf_injection_with_header_injection_attempt.yml` |  |
| 100331 | 7 | converted | `rules/web/http-response-splitting/http_response_splitting_double_crlf_with_html_injection.yml` |  |
| 100340 | 6 | converted | `rules/web/open-redirect/open_redirect_url_parameter_redirecting_to_external_domain.yml` |  |
| 100341 | 6 | converted | `rules/web/open-redirect/open_redirect_protocol_relative_url_redirect_attempt_domain.yml` |  |
| 100342 | 7 | converted | `rules/web/open-redirect/open_redirect_encoded_or_backslash_redirect_bypass_attempt.yml` |  |
| 100350 | 7 | converted | `rules/web/crlf-injection/crlf_injection_url_encoded_line_terminator_detected_in_request.yml` |  |
| 100351 | 8 | converted | `rules/web/crlf-injection/crlf_injection_header_injection_via_crlf_in_url_parameter.yml` |  |
| 100360 | 8 | converted | `rules/web/deserialization/deserialization_php_serialized_object_detected_in_url_parameter.yml` |  |
| 100361 | 9 | merged | `rules/web/deserialization/deserialization_java_serialized_object_detected_magic_bytes_ro0abx_ace.yml` |  |
| 100362 | 8 | converted | `rules/web/deserialization/deserialization_python_pickle_yaml_deserialization_pattern_detected.yml` |  |
| 100363 | 9 | merged | `rules/web/deserialization/deserialization_known_java_deserialization_exploit_gadget_chain_detect.yml` |  |
| 100364 | 8 | converted | `rules/web/deserialization/deserialization_net_json_deserialization_type_indicator_detected.yml` |  |
| 100365 | 12 | converted | `rules/correlations/deserialization_repeated_deserialization_attack_attempts.yml` |  |
| 100380 | 8 | converted | `rules/web/ssti/ssti_template_expression_syntax_detected_in_url_jinja2_twig_freemarker.yml` |  |
| 100381 | 9 | converted | `rules/web/ssti/ssti_common_ssti_probe_detected_7_7_config_self.yml` |  |
| 100382 | 10 | converted | `rules/web/ssti/ssti_python_mro_chain_traversal.yml` |  |
| 100383 | 9 | converted | `rules/web/ssti/ssti_spring_java_el_expression_injection.yml` |  |
| 100384 | 9 | converted | `rules/web/ssti/ssti_freemarker_thymeleaf_template_expression_injection.yml` |  |
| 100385 | 8 | converted | `rules/web/ssti/ssti_jinja2_filter_based_bypass_attempt_attr_join_request.yml` |  |
| 100400 | 6 | merged | `rules/web/idor/idor_direct_access_to_user_resource_by_numeric_id.yml` |  |
| 100401 | 10 | converted | `rules/correlations/idor_rapid_sequential_user_id_enumeration.yml` |  |
| 100402 | 7 | merged | `rules/web/idor/idor_file_attachment_access_via_sequential_numeric_id.yml` |  |
| 100403 | 8 | merged | `rules/web/idor/idor_financial_transactional_record_access_by_sequential_id.yml` |  |
| 100404 | 12 | converted | `rules/correlations/idor_mass_file_document_enumeration.yml` |  |
| 100420 | 8 | converted | `rules/web/jwt-attacks/jwt_attack_algorithm_none_detected.yml` |  |
| 100421 | 8 | converted | `rules/web/jwt-attacks/jwt_attack_algorithm_confusion.yml` |  |
| 100422 | 7 | converted | `rules/web/jwt-attacks/jwt_attack_kid_parameter_injection.yml` |  |
| 100423 | 8 | converted | `rules/web/jwt-attacks/jwt_attack_jku_x5u_header_injection.yml` |  |
| 100424 | 7 | converted | `rules/web/jwt-attacks/jwt_attack_suspicious_jwt_claims.yml` |  |
| 100425 | 7 | converted | `rules/web/jwt-attacks/jwt_attack_manipulated_time_claims.yml` |  |
| 100426 | 12 | converted | `rules/correlations/jwt_attack_repeated_jwt_manipulation_attempts.yml` |  |
| 100440 | 7 | converted | `rules/web/graphql-attacks/graphql_attack_introspection_query_detected.yml` |  |
| 100441 | 8 | converted | `rules/web/graphql-attacks/graphql_attack_deeply_nested_query.yml` |  |
| 100442 | 8 | converted | `rules/web/graphql-attacks/graphql_attack_batched_operations.yml` |  |
| 100443 | 7 | converted | `rules/web/graphql-attacks/graphql_attack_recursive_fragment.yml` |  |
| 100444 | 7 | converted | `rules/web/graphql-attacks/graphql_attack_destructive_mutation_attempt_detected.yml` |  |
| 100445 | 9 | converted | `rules/web/graphql-attacks/graphql_attack_alias_based_batching_abuse.yml` |  |
| 100446 | 12 | converted | `rules/correlations/graphql_attack_repeated_graphql_attack_patterns.yml` |  |
| 100460 | 8 | converted | `rules/web/upload-attacks/upload_attack_php_file_upload_attempt_with_executable_extension.yml` |  |
| 100461 | 8 | converted | `rules/web/upload-attacks/upload_attack_asp_aspx_file_upload_attempt.yml` |  |
| 100462 | 8 | converted | `rules/web/upload-attacks/upload_attack_jsp_war_file_upload_attempt.yml` |  |
| 100463 | 9 | converted | `rules/web/upload-attacks/upload_attack_windows_executable_script_file_upload_attempt.yml` |  |
| 100464 | 7 | converted | `rules/web/upload-attacks/upload_attack_svg_html_file_upload.yml` |  |
| 100465 | 8 | converted | `rules/web/upload-attacks/upload_attack_mime_type_mismatch.yml` |  |
| 100466 | 8 | converted | `rules/web/upload-attacks/upload_attack_null_byte_or_double_extension_bypass_attempt.yml` |  |
| 100467 | 7 | converted | `rules/web/upload-attacks/upload_attack_server_configuration_file_upload_attempt_htaccess_web_co.yml` |  |
| 100468 | 12 | converted | `rules/correlations/upload_attack_repeated_malicious_file_upload_attempts.yml` |  |
| 100480 | 8 | converted | `rules/web/wordpress-attacks/wordpress_direct_php_execution_in_plugins_directory.yml` |  |
| 100481 | 8 | converted | `rules/web/wordpress-attacks/wordpress_php_file_in_uploads_directory.yml` |  |
| 100482 | 7 | converted | `rules/web/wordpress-attacks/wordpress_xml_rpc_abuse.yml` |  |
| 100483 | 12 | converted | `rules/correlations/wordpress_aggressive_xml_rpc_brute_force.yml` |  |
| 100484 | 8 | converted | `rules/web/wordpress-attacks/wordpress_rest_api_user_enumeration_attempt.yml` |  |
| 100485 | 6 | converted | `rules/web/wordpress-attacks/wordpress_author_id_enumeration_via_url_parameter.yml` |  |
| 100486 | 9 | converted | `rules/web/wordpress-attacks/wordpress_known_vulnerable_plugin_ajax_action_exploit_attempt.yml` |  |
| 100487 | 7 | converted | `rules/web/wordpress-attacks/wordpress_wp_config_backup_file_access.yml` |  |
| 100488 | 8 | converted | `rules/web/wordpress-attacks/wordpress_direct_wp_includes_core_file_access_with_parameters.yml` |  |
| 100489 | 10 | converted | `rules/correlations/wordpress_repeated_wordpress_targeted_attacks_from_same_ip.yml` |  |
| 100700 | 6 | converted | `rules/web/path-traversal/path_traversal_basic_or_pattern_in_url.yml` |  |
| 100701 | 7 | converted | `rules/web/path-traversal/path_traversal_utf_8_overlong_encoding_bypass_attempt.yml` |  |
| 100702 | 7 | converted | `rules/web/path-traversal/path_traversal_double_url_encoding_bypass_attempt.yml` |  |
| 100703 | 7 | converted | `rules/web/path-traversal/path_traversal_hex_encoding_bypass_attempt.yml` |  |
| 100704 | 8 | converted | `rules/web/path-traversal/path_traversal_deep_traversal_4_levels.yml` |  |
| 100705 | 7 | converted | `rules/web/path-traversal/path_traversal_traversal_targeting_config_backup_key_files.yml` |  |
| 100706 | 10 | converted | `rules/web/path-traversal/path_traversal_traversal_pattern_returned_http.yml` |  |
| 100707 | 6 | converted | `rules/web/api-abuse/api_abuse_rate_limit_triggered_http.yml` |  |
| 100708 | 8 | converted | `rules/web/api-abuse/api_abuse_access_to_administrative_or_internal_api_endpoint.yml` |  |
| 100709 | 7 | converted | `rules/web/api-abuse/api_abuse_sequential_id_enumeration_on_api.yml` |  |
| 100710 | 6 | converted | `rules/web/api-abuse/api_abuse_server_error_on_api_endpoint.yml` |  |
| 100711 | 10 | converted | `rules/web/api-abuse/api_abuse_attack_pattern_returned_http.yml` |  |
| 100712 | 6 | converted | `rules/web/brute-force-web/web_brute_force_failed_login_attempt_401_403_on_auth_endpoint.yml` |  |
| 100713 | 8 | merged | `rules/web/brute-force-web/web_brute_force_failed_cms_admin_login_attempt_wordpress_joomla.yml` |  |
| 100714 | 6 | converted | `rules/web/brute-force-web/web_brute_force_failed_api_authentication_attempt.yml` |  |
| 100715 | 10 | converted | `rules/web/brute-force-web/brute_force_web_attack_pattern_returned_http.yml` |  |
| 100716 | 8 | converted | `rules/web/command-injection/command_injection_pipe_to_recon_command_detected_in_url.yml` |  |
| 100717 | 8 | converted | `rules/web/command-injection/command_injection_semicolon_chained_command_detected_in_url.yml` |  |
| 100718 | 8 | converted | `rules/web/command-injection/command_injection_backtick_or_command_substitution_detected.yml` |  |
| 100719 | 9 | converted | `rules/web/command-injection/command_injection_remote_file_download_attempt_via_wget_curl.yml` |  |
| 100720 | 10 | converted | `rules/web/command-injection/command_injection_reverse_shell_attempt_via_netcat_socat.yml` |  |
| 100721 | 10 | converted | `rules/web/command-injection/command_injection_bash_reverse_shell_pattern_detected.yml` |  |
| 100722 | 8 | converted | `rules/web/command-injection/command_injection_scripting_language_one_liner_execution_attempt.yml` |  |
| 100723 | 8 | converted | `rules/web/command-injection/command_injection_and_chained_command_detected.yml` |  |
| 100724 | 9 | converted | `rules/web/command-injection/command_injection_file_permission_change_attempt_chmod_chown.yml` |  |
| 100725 | 12 | converted | `rules/web/command-injection/command_injection_attack_pattern_returned_http.yml` |  |
| 100726 | 7 | converted | `rules/web/crlf-injection/crlf_injection_url_encoded_line_terminator_detected_in_request.yml` |  |
| 100727 | 8 | converted | `rules/web/crlf-injection/crlf_injection_header_injection_via_crlf_in_url_parameter.yml` |  |
| 100728 | 10 | converted | `rules/web/crlf-injection/crlf_injection_attack_pattern_returned_http.yml` |  |
| 100729 | 6 | converted | `rules/web/csrf/csrf_state_changing_request_with_csrf_token_but_missing_referer_header.yml` |  |
| 100729 | 6 | private (overwrite) |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100730 | 7 | merged | `rules/web/csrf/csrf_post_to_sensitive_api_endpoint.yml` |  |
| 100731 | 8 | converted | `rules/web/csrf/csrf_successful_access_to_account_management_endpoint.yml` |  |
| 100732 | 10 | converted | `rules/web/csrf/csrf_attack_pattern_returned_http.yml` |  |
| 100733 | 8 | converted | `rules/web/deserialization/deserialization_php_serialized_object_detected_in_url_parameter.yml` |  |
| 100734 | 9 | converted | `rules/web/deserialization/deserialization_java_serialized_object_detected_magic_bytes_ro0abx_ace.yml` |  |
| 100735 | 8 | converted | `rules/web/deserialization/deserialization_python_pickle_yaml_deserialization_pattern_detected.yml` |  |
| 100736 | 9 | converted | `rules/web/deserialization/deserialization_known_java_deserialization_exploit_gadget_chain_detect.yml` |  |
| 100737 | 8 | converted | `rules/web/deserialization/deserialization_net_json_deserialization_type_indicator_detected.yml` |  |
| 100738 | 11 | converted | `rules/web/deserialization/deserialization_attack_pattern_returned_http.yml` |  |
| 100739 | 7 | converted | `rules/web/graphql-attacks/graphql_attack_introspection_query_detected.yml` |  |
| 100740 | 8 | converted | `rules/web/graphql-attacks/graphql_attack_deeply_nested_query.yml` |  |
| 100741 | 8 | converted | `rules/web/graphql-attacks/graphql_attack_batched_operations.yml` |  |
| 100742 | 7 | converted | `rules/web/graphql-attacks/graphql_attack_recursive_fragment.yml` |  |
| 100743 | 7 | converted | `rules/web/graphql-attacks/graphql_attack_destructive_mutation_attempt_detected.yml` |  |
| 100744 | 9 | converted | `rules/web/graphql-attacks/graphql_attack_alias_based_batching_abuse.yml` |  |
| 100745 | 11 | converted | `rules/web/graphql-attacks/graphql_attacks_attack_pattern_returned_http.yml` |  |
| 100746 | 7 | converted | `rules/web/http-response-splitting/http_response_splitting_crlf_injection_with_header_injection_attempt.yml` |  |
| 100747 | 7 | converted | `rules/web/http-response-splitting/http_response_splitting_double_crlf_with_html_injection.yml` |  |
| 100748 | 10 | converted | `rules/web/http-response-splitting/http_response_splitting_attack_pattern_returned_http.yml` |  |
| 100749 | 8 | converted | `rules/web/http-smuggling/http_smuggling_both_transfer_encoding_and_content_length_headers.yml` |  |
| 100750 | 8 | converted | `rules/web/http-smuggling/http_smuggling_obfuscated_transfer_encoding_header_value.yml` |  |
| 100751 | 7 | converted | `rules/web/http-smuggling/http_smuggling_embedded_http_request_detected_within_body.yml` |  |
| 100752 | 7 | converted | `rules/web/http-smuggling/http_smuggling_duplicate_content_length_headers_detected.yml` |  |
| 100753 | 10 | converted | `rules/web/http-smuggling/http_smuggling_attack_pattern_returned_http.yml` |  |
| 100754 | 6 | converted | `rules/web/idor/idor_direct_access_to_user_resource_by_numeric_id.yml` |  |
| 100755 | 7 | converted | `rules/web/idor/idor_file_attachment_access_via_sequential_numeric_id.yml` |  |
| 100756 | 8 | converted | `rules/web/idor/idor_financial_transactional_record_access_by_sequential_id.yml` |  |
| 100757 | 10 | converted | `rules/web/idor/idor_attack_pattern_returned_http.yml` |  |
| 100758 | 8 | converted | `rules/web/jwt-attacks/jwt_attack_algorithm_none_detected.yml` |  |
| 100759 | 8 | converted | `rules/web/jwt-attacks/jwt_attack_algorithm_confusion.yml` |  |
| 100760 | 7 | converted | `rules/web/jwt-attacks/jwt_attack_kid_parameter_injection.yml` |  |
| 100761 | 8 | converted | `rules/web/jwt-attacks/jwt_attack_jku_x5u_header_injection.yml` |  |
| 100762 | 7 | converted | `rules/web/jwt-attacks/jwt_attack_suspicious_jwt_claims.yml` |  |
| 100763 | 7 | converted | `rules/web/jwt-attacks/jwt_attack_manipulated_time_claims.yml` |  |
| 100764 | 10 | converted | `rules/web/jwt-attacks/jwt_attacks_attack_pattern_returned_http.yml` |  |
| 100765 | 6 | converted | `rules/web/open-redirect/open_redirect_url_parameter_redirecting_to_external_domain.yml` |  |
| 100766 | 6 | converted | `rules/web/open-redirect/open_redirect_protocol_relative_url_redirect_attempt_domain.yml` |  |
| 100767 | 7 | converted | `rules/web/open-redirect/open_redirect_encoded_or_backslash_redirect_bypass_attempt.yml` |  |
| 100768 | 10 | converted | `rules/web/open-redirect/open_redirect_attack_pattern_returned_http.yml` |  |
| 100769 | 8 | converted | `rules/web/rfi-lfi/rfi_remote_file_inclusion_attempt_via_url_parameter_with_protocol_sche.yml` |  |
| 100770 | 7 | converted | `rules/web/rfi-lfi/rfi_php_stream_wrapper_abuse_php_filter_php_input_php_data.yml` |  |
| 100771 | 7 | converted | `rules/web/rfi-lfi/rfi_exotic_php_wrapper_detected_expect_zip_phar_glob.yml` |  |
| 100772 | 7 | converted | `rules/web/rfi-lfi/lfi_deep_directory_traversal_attempt_3_levels.yml` |  |
| 100773 | 8 | converted | `rules/web/rfi-lfi/lfi_attempted_access_to_sensitive_unix_system_files.yml` |  |
| 100774 | 8 | converted | `rules/web/rfi-lfi/lfi_proc_self_access_attempt.yml` |  |
| 100775 | 7 | converted | `rules/web/rfi-lfi/lfi_windows_system_file_access_attempt.yml` |  |
| 100776 | 7 | converted | `rules/web/rfi-lfi/lfi_sensitive_configuration_file_access_attempt.yml` |  |
| 100777 | 7 | converted | `rules/web/rfi-lfi/lfi_log_file_inclusion_attempt.yml` |  |
| 100778 | 10 | converted | `rules/web/rfi-lfi/rfi_lfi_attack_pattern_returned_http.yml` |  |
| 100779 | 6 | converted | `rules/web/sql-injection/sql_injection_union_select_or_select_from_where_pattern_detected_in_ur.yml` |  |
| 100780 | 6 | converted | `rules/web/sql-injection/sql_injection_or_based_injection_attempt_via_encoded_characters.yml` |  |
| 100781 | 8 | converted | `rules/web/sql-injection/sql_injection_stored_procedure_execution_attempt_sp_xp.yml` |  |
| 100782 | 8 | converted | `rules/web/sql-injection/sql_injection_destructive_ddl_statement_detected_drop_truncate_alter_t.yml` |  |
| 100783 | 6 | converted | `rules/web/sql-injection/sql_injection_database_metadata_enumeration_attempt.yml` |  |
| 100784 | 6 | converted | `rules/web/sql-injection/sql_injection_time_based_blind_injection_attempt_sleep_benchmark_waitf.yml` |  |
| 100785 | 7 | converted | `rules/web/sql-injection/sql_injection_file_read_write_attempt_via_sql_load_file_into_outfile.yml` |  |
| 100786 | 10 | converted | `rules/web/sql-injection/sql_injection_error_based_injection_via_having_group_by_with_aggregate.yml` |  |
| 100787 | 6 | converted | `rules/web/sql-injection/sql_injection_sql_comment_terminator_detected_at_end_of_parameter.yml` |  |
| 100788 | 7 | converted | `rules/web/sql-injection/sql_injection_cast_convert_type_coercion_detected_in_url.yml` |  |
| 100789 | 7 | converted | `rules/web/sql-injection/sql_injection_string_function_abuse_detected_char_concat_group_concat.yml` |  |
| 100790 | 12 | converted | `rules/web/sql-injection/sql_injection_attack_pattern_returned_http.yml` |  |
| 100791 | 8 | converted | `rules/web/ssrf/ssrf_request_to_localhost_loopback_via_url_parameter.yml` |  |
| 100792 | 8 | converted | `rules/web/ssrf/ssrf_request_targeting_internal_rfc1918_address_range.yml` |  |
| 100793 | 9 | converted | `rules/web/ssrf/ssrf_cloud_metadata_endpoint_169_254_169_254_access_attempt.yml` |  |
| 100794 | 8 | converted | `rules/web/ssrf/ssrf_ipv6_loopback_address_1_access_attempt.yml` |  |
| 100795 | 8 | converted | `rules/web/ssrf/ssrf_exotic_protocol_scheme_gopher_dict_ldap_tftp.yml` |  |
| 100796 | 8 | converted | `rules/web/ssrf/ssrf_url_with_embedded_credentials.yml` |  |
| 100797 | 8 | converted | `rules/web/ssrf/ssrf_obfuscated_localhost_via_decimal_octal_hex_ip_representation.yml` |  |
| 100798 | 9 | converted | `rules/web/ssrf/ssrf_cloud_instance_metadata_path_detected_aws_gcp_azure.yml` |  |
| 100799 | 11 | converted | `rules/web/ssrf/ssrf_attack_pattern_returned_http.yml` |  |
| 100800 | 8 | converted | `rules/web/ssti/ssti_template_expression_syntax_detected_in_url_jinja2_twig_freemarker.yml` |  |
| 100801 | 9 | converted | `rules/web/ssti/ssti_common_ssti_probe_detected_7_7_config_self.yml` |  |
| 100802 | 10 | converted | `rules/web/ssti/ssti_python_mro_chain_traversal.yml` |  |
| 100803 | 9 | converted | `rules/web/ssti/ssti_spring_java_el_expression_injection.yml` |  |
| 100804 | 9 | converted | `rules/web/ssti/ssti_freemarker_thymeleaf_template_expression_injection.yml` |  |
| 100805 | 8 | converted | `rules/web/ssti/ssti_jinja2_filter_based_bypass_attempt_attr_join_request.yml` |  |
| 100806 | 12 | converted | `rules/web/ssti/ssti_attack_pattern_returned_http.yml` |  |
| 100807 | 8 | converted | `rules/web/upload-attacks/upload_attack_php_file_upload_attempt_with_executable_extension.yml` |  |
| 100808 | 8 | converted | `rules/web/upload-attacks/upload_attack_asp_aspx_file_upload_attempt.yml` |  |
| 100809 | 8 | converted | `rules/web/upload-attacks/upload_attack_jsp_war_file_upload_attempt.yml` |  |
| 100810 | 9 | converted | `rules/web/upload-attacks/upload_attack_windows_executable_script_file_upload_attempt.yml` |  |
| 100811 | 7 | converted | `rules/web/upload-attacks/upload_attack_svg_html_file_upload.yml` |  |
| 100812 | 8 | converted | `rules/web/upload-attacks/upload_attack_mime_type_mismatch.yml` |  |
| 100813 | 8 | converted | `rules/web/upload-attacks/upload_attack_null_byte_or_double_extension_bypass_attempt.yml` |  |
| 100814 | 7 | converted | `rules/web/upload-attacks/upload_attack_server_configuration_file_upload_attempt_htaccess_web_co.yml` |  |
| 100815 | 11 | converted | `rules/web/upload-attacks/upload_attacks_attack_pattern_returned_http.yml` |  |
| 100816 | 10 | converted | `rules/web/web-shell/web_shell_known_web_shell_filename_detected_in_url.yml` |  |
| 100817 | 9 | converted | `rules/web/web-shell/web_shell_command_parameter_pattern_detected.yml` |  |
| 100818 | 10 | converted | `rules/web/web-shell/web_shell_php_shell_code_pattern_eval_system_with_superglobal.yml` |  |
| 100819 | 9 | converted | `rules/web/web-shell/web_shell_php_dangerous_function_call_detected_in_url.yml` |  |
| 100820 | 10 | converted | `rules/web/web-shell/web_shell_obfuscation_function_detected.yml` |  |
| 100821 | 9 | converted | `rules/web/web-shell/web_shell_server_side_script_accessed_from_upload_images_directory.yml` |  |
| 100822 | 9 | converted | `rules/web/web-shell/web_shell_double_extension_detected.yml` |  |
| 100823 | 12 | converted | `rules/web/web-shell/web_shell_attack_pattern_returned_http.yml` |  |
| 100824 | 8 | converted | `rules/web/wordpress-attacks/wordpress_direct_php_execution_in_plugins_directory.yml` |  |
| 100825 | 8 | converted | `rules/web/wordpress-attacks/wordpress_php_file_in_uploads_directory.yml` |  |
| 100826 | 7 | converted | `rules/web/wordpress-attacks/wordpress_xml_rpc_abuse.yml` |  |
| 100827 | 8 | converted | `rules/web/wordpress-attacks/wordpress_rest_api_user_enumeration_attempt.yml` |  |
| 100828 | 6 | converted | `rules/web/wordpress-attacks/wordpress_author_id_enumeration_via_url_parameter.yml` |  |
| 100829 | 9 | converted | `rules/web/wordpress-attacks/wordpress_known_vulnerable_plugin_ajax_action_exploit_attempt.yml` |  |
| 100830 | 7 | converted | `rules/web/wordpress-attacks/wordpress_wp_config_backup_file_access.yml` |  |
| 100831 | 8 | converted | `rules/web/wordpress-attacks/wordpress_direct_wp_includes_core_file_access_with_parameters.yml` |  |
| 100832 | 11 | converted | `rules/web/wordpress-attacks/wordpress_attacks_attack_pattern_returned_http.yml` |  |
| 100833 | 6 | converted | `rules/web/xss/xss_script_tag_detected_in_url_parameter.yml` |  |
| 100834 | 6 | converted | `rules/web/xss/xss_event_handler_injection_attempt.yml` |  |
| 100835 | 6 | converted | `rules/web/xss/xss_javascript_or_vbscript_uri_scheme_injection_attempt.yml` |  |
| 100836 | 7 | converted | `rules/web/xss/xss_embedded_content_tag_injection.yml` |  |
| 100837 | 6 | converted | `rules/web/xss/xss_tag_with_event_handler_injection.yml` |  |
| 100838 | 6 | converted | `rules/web/xss/xss_dom_based_xss_object_access_in_url.yml` |  |
| 100839 | 6 | converted | `rules/web/xss/xss_javascript_function_injection.yml` |  |
| 100840 | 7 | converted | `rules/web/xss/xss_css_based_injection_attempt.yml` |  |
| 100841 | 6 | converted | `rules/web/xss/xss_data_uri_with_html_content_type_detected.yml` |  |
| 100842 | 10 | converted | `rules/web/xss/xss_attack_pattern_returned_http.yml` |  |
| 100843 | 8 | converted | `rules/web/xxe/xxe_doctype_entity_declaration_detected_in_request.yml` |  |
| 100844 | 9 | converted | `rules/web/xxe/xxe_system_entity_with_external_uri.yml` |  |
| 100845 | 8 | converted | `rules/web/xxe/xxe_public_entity_with_external_dtd_reference_detected.yml` |  |
| 100846 | 9 | converted | `rules/web/xxe/xxe_parameter_entity_declaration.yml` |  |
| 100847 | 8 | converted | `rules/web/xxe/xxe_xml_declaration_followed_by_doctype.yml` |  |
| 100848 | 9 | converted | `rules/web/xxe/xxe_entity_referencing_etc_passwd_or_file.yml` |  |
| 100849 | 10 | converted | `rules/web/xxe/xxe_entity_with_command_execution_or_php_filter_wrapper.yml` |  |
| 100850 | 12 | converted | `rules/web/xxe/xxe_attack_pattern_returned_http.yml` |  |
| 100900 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100901 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100902 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100904 | 0 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100905 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100906 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100907 | 5 | not converted |  | Site-specific downgrade of a correlation. Sigma filters do not apply to correlation rules. |
| 100908 | 0 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100910 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100911 | 3 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100912 | 3 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100913 | 3 | not converted |  | Site-specific downgrade of a correlation. Sigma filters do not apply to correlation rules. |
| 100914 | 10 | not converted |  | Site-specific detection. Kept private. |
| 100915 | 3 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100916 | 3 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100917 | 3 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100918 | 3 | not converted |  | Site-specific downgrade of a correlation. Sigma filters do not apply to correlation rules. |
| 100919 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100920 | 3 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100921 | 3 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100922 | 3 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100923 | 3 | filter | `filters/static_svg_html_get_not_an_upload.yml` |  |
| 100924 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100925 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100955 | 3 | filter | `filters/static_svg_html_get_not_an_upload.yml` |  |
| 100956 | 3 | filter | `filters/static_svg_html_get_not_an_upload.yml` |  |
| 100960 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100961 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100962 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100963 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100964 | 0 | not converted |  | Tuning of a Wazuh built-in rule (silence, downgrade or level change). No Sigma rule to attach a filter to. |
| 100965 | 0 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
| 100966 | 10 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
| 100967 | 7 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
| 100968 | 3 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
| 100970 | 3 | not converted |  | Exclusion for a regex branch the public rule no longer has (the FP-fixed form was kept). |
| 100971 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100972 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100973 | 3 | filter | `filters/dotcom_word_in_path_not_a_com_file.yml` |  |
| 100974 | 3 | filter | `filters/dotcom_word_in_path_not_a_com_file.yml` |  |
| 100986 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100987 | 3 | filter | `filters/binary_tls_bytes_on_plain_http_port.yml` |  |
| 100988 | 3 | filter | `filters/dotenv_inside_a_word_in_query_value.yml` |  |
| 100989 | 3 | filter | `filters/uuid_record_ids_are_not_enumerable.yml` |  |
| 100990 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 100991 | 3 | not converted |  | Site-specific exclusion. Kept in a private filter overlay. |
| 101000 | 8 | converted | `rules/web/initial-access/exploit_public_facing_application_struts_ognl_expression_injection.yml` |  |
| 101001 | 9 | converted | `rules/web/initial-access/exploit_public_facing_application_log4shell_cve_2021_44228_jndi_inject.yml` |  |
| 101002 | 9 | converted | `rules/web/initial-access/exploit_public_facing_application_obfuscated_log4shell_bypass_attempt.yml` |  |
| 101003 | 8 | converted | `rules/web/initial-access/exploit_public_facing_application_shellshock_cve_2014_6271_attempt.yml` |  |
| 101004 | 8 | converted | `rules/web/initial-access/exploit_public_facing_application_vcs_metadata_exposure_git_svn.yml` |  |
| 101005 | 10 | converted | `rules/linux/initial-access/valid_accounts_ssh_authentication_failure.yml` |  |
| 101006 | 12 | converted | `rules/correlations/valid_accounts_brute_force_against_ssh_from_single_source.yml` |  |
| 101007 | 8 | converted | `rules/web/initial-access/exploit_public_facing_application_spring_boot_actuator_endpoint_access.yml` |  |
| 101008 | 8 | converted | `rules/web/initial-access/exploit_public_facing_application_java_application_server_admin_consol.yml` |  |
| 101009 | 9 | converted | `rules/web/initial-access/exploit_public_facing_application_apache_solr_injection_attempt.yml` |  |
| 101010 | 8 | converted | `rules/web/initial-access/exploit_public_facing_application_exchange_proxyshell_proxylogon_probe.yml` |  |
| 101011 | 7 | converted | `rules/linux/initial-access/external_remote_services_ssh_login_from_external_public_ip_address.yml` |  |
| 101012 | 10 | converted | `rules/linux/initial-access/valid_accounts_root_login_via_ssh.yml` |  |
| 101050 | 10 | converted | `rules/linux/execution/powershell_encoded_command_execution_detected.yml` |  |
| 101051 | 9 | converted | `rules/linux/execution/powershell_suspicious_cmdlet_execution_iex_invoke_webrequest.yml` |  |
| 101052 | 9 | converted | `rules/linux/execution/powershell_download_cradle_or_socket_connection_attempt.yml` |  |
| 101053 | 8 | converted | `rules/linux/execution/unix_shell_download_and_execute_pipe_pattern.yml` |  |
| 101054 | 9 | converted | `rules/linux/execution/python_interactive_python_reverse_shell_or_command_execution.yml` |  |
| 101055 | 10 | converted | `rules/linux/execution/scheduled_task_cron_crontab_modification_with_download_execution_comma.yml` |  |
| 101056 | 8 | converted | `rules/linux/execution/scheduled_task_at_at_command_scheduling_suspicious_execution.yml` |  |
| 101057 | 10 | converted | `rules/linux/execution/system_binary_proxy_execution_lolbin_abuse_mshta_regsvr32_rundll32.yml` |  |
| 101058 | 9 | converted | `rules/linux/execution/wmi_windows_management_instrumentation_command_execution.yml` |  |
| 101059 | 8 | converted | `rules/linux/execution/system_binary_proxy_execution_certutil_bitsadmin_download_abuse.yml` |  |
| 101060 | 9 | converted | `rules/linux/execution/visual_basic_jscript_script_host_executing_vbs_js_file.yml` |  |
| 101061 | 10 | converted | `rules/linux/execution/command_and_scripting_interpreter_dns_server_administration_command.yml` |  |
| 101100 | 10 | converted | `rules/linux/persistence/cron_new_or_modified_cron_job_detected.yml` |  |
| 101101 | 10 | converted | `rules/linux/persistence/cron_system_crontab_modified.yml` |  |
| 101102 | 12 | converted | `rules/linux/persistence/ssh_authorized_keys_modification_of_ssh_authorized_keys_file.yml` |  |
| 101103 | 10 | converted | `rules/linux/persistence/boot_logon_init_scripts_startup_script_or_systemd_service_modified.yml` |  |
| 101104 | 10 | converted | `rules/linux/persistence/unix_shell_config_shell_profile_rc_file_modified.yml` |  |
| 101105 | 12 | converted | `rules/linux/persistence/create_account_user_group_database_file_modified.yml` |  |
| 101106 | 10 | converted | `rules/linux/persistence/create_account_new_user_created_or_user_added_to_privileged_group.yml` |  |
| 101107 | 10 | converted | `rules/linux/persistence/sudo_policy_sudoers_file_modified.yml` |  |
| 101108 | 10 | converted | `rules/linux/persistence/ld_preload_shared_library_preload_configuration_modified.yml` |  |
| 101109 | 12 | converted | `rules/linux/persistence/pam_modification_pam_module_configuration_modified.yml` |  |
| 101110 | 10 | converted | `rules/linux/persistence/systemd_service_system_level_systemd_service_timer_created_or_modified.yml` |  |
| 101111 | 9 | converted | `rules/linux/persistence/systemd_service_service_enabled_via_systemctl.yml` |  |
| 101112 | 10 | converted | `rules/linux/persistence/rc_scripts_message_of_the_day_scripts_modified.yml` |  |
| 101150 | 10 | converted | `rules/linux/privilege-escalation/sudo_abuse_sudo_used_to_execute_shell_or_modify_credentials.yml` |  |
| 101151 | 12 | converted | `rules/linux/privilege-escalation/sudo_abuse_root_shell_obtained_via_sudo.yml` |  |
| 101152 | 10 | converted | `rules/linux/privilege-escalation/setuid_setgid_suid_sgid_bit_set_on_file.yml` |  |
| 101153 | 10 | converted | `rules/linux/privilege-escalation/setuid_setgid_enumeration_of_suid_sgid_binaries.yml` |  |
| 101154 | 10 | converted | `rules/linux/privilege-escalation/valid_accounts_switch_to_root_user_via_su_command.yml` |  |
| 101155 | 12 | hand | `rules/linux/privilege-escalation/sudo_segfault.yml` |  |
| 101156 | 10 | converted | `rules/linux/privilege-escalation/abuse_elevation_control_linux_capabilities_manipulation_detected.yml` |  |
| 101157 | 10 | converted | `rules/linux/privilege-escalation/exploitation_for_privilege_escalation_polkit_pkexec_exploitation_attem.yml` |  |
| 101158 | 9 | converted | `rules/linux/privilege-escalation/escape_to_host_container_escape_attempt_via_nsenter_unshare.yml` |  |
| 101159 | 12 | converted | `rules/linux/privilege-escalation/escape_to_host_privileged_docker_container_launched_or_interactive_exe.yml` |  |
| 101160 | 10 | converted | `rules/linux/privilege-escalation/process_injection_ptrace_strace_attaching_to_running_process.yml` |  |
| 101200 | 12 | converted | `rules/linux/defense-evasion/clear_linux_logs_log_file_deletion_or_truncation_detected.yml` |  |
| 101201 | 10 | converted | `rules/linux/defense-evasion/disable_or_modify_tools_security_logging_service_stopped_or_disabled.yml` |  |
| 101202 | 12 | converted | `rules/linux/defense-evasion/disable_or_modify_tools_ids_ips_or_hids_agent_stopped.yml` |  |
| 101203 | 10 | converted | `rules/linux/defense-evasion/disable_or_modify_firewall_firewall_rules_flushed_or_deleted.yml` |  |
| 101204 | 10 | converted | `rules/linux/defense-evasion/disable_security_ufw_firewalld_disabled_or_selinux_set_to_permissive.yml` |  |
| 101205 | 10 | converted | `rules/linux/defense-evasion/clear_command_history_shell_history_cleared_or_logging_disabled.yml` |  |
| 101206 | 10 | converted | `rules/linux/defense-evasion/timestomp_file_timestamp_manipulation_detected.yml` |  |
| 101207 | 9 | converted | `rules/linux/defense-evasion/deobfuscate_decode_payload_decoding_via_base64_openssl_xxd.yml` |  |
| 101208 | 10 | converted | `rules/linux/defense-evasion/stored_data_manipulation_dns_configuration_file_modified.yml` |  |
| 101209 | 10 | converted | `rules/linux/defense-evasion/indicator_removal_security_evidence_files_being_deleted.yml` |  |
| 101210 | 9 | converted | `rules/linux/defense-evasion/hijack_execution_ld_preload_environment_variable_set.yml` |  |
| 101211 | 10 | converted | `rules/linux/defense-evasion/disable_audit_audit_daemon_killed_or_rules_cleared.yml` |  |
| 101212 | 9 | converted | `rules/linux/defense-evasion/impair_defenses_log_directory_bind_mounted_to_dev_null.yml` |  |
| 101250 | 12 | converted | `rules/linux/credential-access/os_credential_dumping_etc_shadow_file_read_attempt.yml` |  |
| 101251 | 10 | converted | `rules/linux/credential-access/brute_force_password_cracking_tool_execution_detected.yml` |  |
| 101252 | 12 | converted | `rules/linux/credential-access/os_credential_dumping_mimikatz_or_credential_dumping_tool_detected.yml` |  |
| 101253 | 10 | converted | `rules/linux/credential-access/network_sniffing_traffic_capture_on_credential_bearing_protocols.yml` |  |
| 101254 | 9 | converted | `rules/linux/credential-access/credentials_in_files_grep_search_for_credentials_in_config_files.yml` |  |
| 101255 | 9 | converted | `rules/linux/credential-access/private_keys_search_for_ssh_tls_private_key_files.yml` |  |
| 101256 | 10 | converted | `rules/linux/credential-access/keylogging_keylogger_or_input_capture_tool_detected.yml` |  |
| 101257 | 10 | converted | `rules/linux/credential-access/bash_history_shell_application_history_file_read.yml` |  |
| 101258 | 9 | converted | `rules/linux/credential-access/adversary_in_the_middle_mitm_tool_execution_detected.yml` |  |
| 101259 | 10 | converted | `rules/linux/credential-access/kerberoasting_kerberos_ticket_extraction_tool_detected.yml` |  |
| 101260 | 9 | converted | `rules/linux/credential-access/container_api_environment_variable_dumping.yml` |  |
| 101300 | 6 | converted | `rules/linux/discovery/system_information_discovery_os_kernel_version_enumeration.yml` |  |
| 101301 | 6 | converted | `rules/linux/discovery/system_network_configuration_network_configuration_enumeration.yml` |  |
| 101302 | 7 | converted | `rules/linux/discovery/remote_system_discovery_network_host_neighbor_enumeration.yml` |  |
| 101303 | 8 | converted | `rules/linux/discovery/network_service_discovery_aggressive_nmap_scan_with_service_version_de.yml` |  |
| 101304 | 6 | converted | `rules/linux/discovery/system_owner_user_discovery_user_enumeration_commands_executed.yml` |  |
| 101305 | 7 | converted | `rules/linux/discovery/account_discovery_local_account_group_enumeration.yml` |  |
| 101306 | 6 | converted | `rules/linux/discovery/process_discovery_process_listing_command_executed.yml` |  |
| 101307 | 6 | converted | `rules/linux/discovery/system_information_discovery_disk_mount_enumeration.yml` |  |
| 101308 | 7 | converted | `rules/linux/discovery/file_and_directory_discovery_broad_filesystem_search_for_sensitive_fil.yml` |  |
| 101309 | 7 | converted | `rules/linux/discovery/software_discovery_installed_packages_enumeration.yml` |  |
| 101310 | 12 | converted | `rules/correlations/discovery_multiple_reconnaissance_commands_in_rapid_succession.yml` |  |
| 101311 | 7 | converted | `rules/linux/discovery/remote_system_discovery_dns_zone_transfer_or_enumeration_attempt.yml` |  |
| 101350 | 8 | converted | `rules/linux/lateral-movement/remote_services_ssh_outbound_ssh_connection_to_ip_address.yml` |  |
| 101351 | 8 | converted | `rules/linux/lateral-movement/remote_services_ssh_sshpass_or_ssh_copy_id_used.yml` |  |
| 101352 | 8 | converted | `rules/linux/lateral-movement/remote_services_file_transfer_via_scp_sftp_rsync_to_remote_host.yml` |  |
| 101353 | 9 | converted | `rules/linux/lateral-movement/smb_admin_shares_remote_execution_tool_detected_psexec_wmi_smb.yml` |  |
| 101354 | 8 | converted | `rules/linux/lateral-movement/remote_desktop_rdp_client_tool_executed.yml` |  |
| 101355 | 9 | converted | `rules/linux/lateral-movement/remote_services_impacket_toolkit_execution_detected.yml` |  |
| 101356 | 8 | converted | `rules/linux/lateral-movement/remote_services_crackmapexec_netexec_lateral_movement_tool_detected.yml` |  |
| 101357 | 8 | converted | `rules/linux/lateral-movement/smb_shares_smb_cifs_share_mounting_or_access.yml` |  |
| 101358 | 9 | converted | `rules/linux/lateral-movement/windows_remote_management_winrm_lateral_movement_attempt.yml` |  |
| 101359 | 10 | converted | `rules/correlations/lateral_movement_multiple_lateral_movement_techniques_from_same_source.yml` |  |
| 101400 | 8 | converted | `rules/linux/collection/archive_collected_data_tar_archive_of_sensitive_directories_created.yml` |  |
| 101401 | 8 | converted | `rules/linux/collection/archive_collected_data_zip_7z_archive_of_sensitive_directories.yml` |  |
| 101402 | 9 | converted | `rules/linux/collection/data_from_local_system_database_dump_command_executed.yml` |  |
| 101403 | 8 | converted | `rules/linux/collection/screen_capture_screenshot_tool_executed.yml` |  |
| 101404 | 9 | converted | `rules/linux/collection/network_sniffing_packet_capture_to_file_initiated.yml` |  |
| 101405 | 7 | converted | `rules/linux/collection/data_from_local_system_bulk_document_collection_via_find_copy.yml` |  |
| 101406 | 8 | converted | `rules/linux/collection/audio_capture_audio_recording_tool_executed.yml` |  |
| 101407 | 8 | converted | `rules/linux/collection/video_capture_video_webcam_capture_tool_executed.yml` |  |
| 101408 | 9 | converted | `rules/linux/collection/clipboard_data_clipboard_content_extraction_tool_detected.yml` |  |
| 101450 | 10 | converted | `rules/linux/command-and-control/non_application_layer_protocol_reverse_bind_shell_via_netcat_socat.yml` |  |
| 101451 | 10 | converted | `rules/linux/command-and-control/non_application_layer_protocol_bash_dev_tcp_reverse_shell.yml` |  |
| 101452 | 9 | converted | `rules/linux/command-and-control/dns_tunneling_dns_tunneling_or_c2_framework_tool_detected.yml` |  |
| 101453 | 9 | converted | `rules/linux/command-and-control/protocol_tunneling_tunnel_proxy_tool_detected_chisel_ngrok_frp_socat.yml` |  |
| 101454 | 9 | converted | `rules/linux/command-and-control/protocol_tunneling_ssh_tunnel_port_forwarding_established.yml` |  |
| 101455 | 10 | converted | `rules/linux/command-and-control/multi_hop_proxy_tor_proxychains_shadowsocks_anonymization_tool_detecte.yml` |  |
| 101456 | 9 | converted | `rules/linux/command-and-control/web_protocols_large_encoded_cookie_in_http_request.yml` |  |
| 101457 | 9 | converted | `rules/linux/command-and-control/remote_access_software_known_c2_framework_rat_tool_detected.yml` |  |
| 101458 | 8 | converted | `rules/linux/command-and-control/proxy_socks_stunnel_proxy_tool_execution_detected.yml` |  |
| 101459 | 8 | converted | `rules/linux/command-and-control/non_application_layer_protocol_icmp_tunnel_covert_channel_attempt.yml` |  |
| 101500 | 9 | converted | `rules/linux/exfiltration/exfiltration_over_alternative_protocol_file_upload_via_curl.yml` |  |
| 101501 | 9 | converted | `rules/linux/exfiltration/exfiltration_over_alternative_protocol_data_file_post_upload_detected.yml` |  |
| 101502 | 10 | converted | `rules/linux/exfiltration/exfiltration_over_alternative_protocol_database_archive_exfiltration_v.yml` |  |
| 101503 | 9 | converted | `rules/linux/exfiltration/exfiltration_to_cloud_storage_rclone_transfer_to_cloud_provider.yml` |  |
| 101504 | 8 | converted | `rules/linux/exfiltration/exfiltration_to_cloud_storage_aws_s3_gcs_file_upload.yml` |  |
| 101505 | 9 | converted | `rules/linux/exfiltration/exfiltration_over_unencrypted_protocol_ftp_file_transfer_to_external_i.yml` |  |
| 101506 | 8 | converted | `rules/linux/exfiltration/exfiltration_over_alternative_protocol_file_piped_through_netcat_to_re.yml` |  |
| 101507 | 9 | converted | `rules/linux/exfiltration/exfiltration_raw_disk_read_piped_to_network_tool.yml` |  |
| 101508 | 8 | converted | `rules/linux/exfiltration/data_transfer_size_limits_large_file_split_into_chunks.yml` |  |
| 101509 | 9 | converted | `rules/linux/exfiltration/exfiltration_encoded_data_piped_to_network_tool.yml` |  |
| 101510 | 12 | converted | `rules/correlations/exfiltration_multiple_exfiltration_indicators_from_same_host.yml` |  |
| 101550 | 14 | converted | `rules/linux/impact/data_destruction_recursive_deletion_of_critical_system_directories.yml` |  |
| 101551 | 14 | converted | `rules/linux/impact/disk_wipe_disk_content_overwrite_via_dd.yml` |  |
| 101552 | 12 | converted | `rules/linux/impact/data_destruction_secure_file_deletion_tool_used_shred_wipe_srm.yml` |  |
| 101553 | 14 | converted | `rules/linux/impact/data_encrypted_for_impact_file_encryption_detected.yml` |  |
| 101554 | 14 | converted | `rules/linux/impact/data_encrypted_for_impact_ransomware_file_extension_detected.yml` |  |
| 101555 | 10 | hand | `rules/correlations/mass_file_modification_possible_ransomware.yml` |  |
| 101556 | 12 | converted | `rules/linux/impact/service_stop_critical_service_forcefully_killed.yml` |  |
| 101557 | 12 | converted | `rules/linux/impact/service_stop_critical_infrastructure_service_stopped_disabled.yml` |  |
| 101558 | 14 | converted | `rules/linux/impact/disk_wipe_filesystem_format_or_partition_deletion_detected.yml` |  |
| 101559 | 10 | converted | `rules/linux/impact/endpoint_dos_resource_exhaustion_or_fork_bomb_detected.yml` |  |
| 101561 | 10 | converted | `rules/linux/impact/resource_hijacking_cryptocurrency_miner_detected.yml` |  |
| 101562 | 12 | converted | `rules/linux/impact/defacement_ransom_message_broadcast_to_system_users_via_wall.yml` |  |
| 101601 | 7 | converted | `rules/web/reconnaissance/active_scanning_server_information_disclosure_page_probed.yml` |  |
| 101602 | 7 | converted | `rules/web/reconnaissance/active_scanning_admin_panel_discovery.yml` |  |
| 101604 | 7 | converted | `rules/web/reconnaissance/active_scanning_backup_test_staging_directory_probed.yml` |  |
| 101605 | 6 | converted | `rules/web/reconnaissance/active_scanning_backup_file_extension_probed_bak_old_swp.yml` |  |
| 101606 | 7 | hand | `rules/web/reconnaissance/known_scanner_user_agent.yml` |  |
| 101607 | 8 | converted | `rules/web/reconnaissance/active_scanning_cloud_devops_configuration_file_probed.yml` |  |
| 101608 | 7 | converted | `rules/web/reconnaissance/active_scanning_api_documentation_health_endpoint_probed.yml` |  |
| 101609 | 10 | converted | `rules/correlations/reconnaissance_multiple_recon_indicators_from_same_ip.yml` |  |
| 101650 | 9 | converted | `rules/linux/resource-development/develop_capabilities_metasploit_payload_generation_tool_detected.yml` |  |
| 101651 | 8 | converted | `rules/linux/resource-development/develop_capabilities_exploit_compilation_detected.yml` |  |
| 101652 | 8 | converted | `rules/linux/resource-development/obtain_capabilities_exploit_search_download_tool_detected.yml` |  |
| 101653 | 8 | converted | `rules/linux/resource-development/obtain_capabilities_offensive_tool_repository_cloned_from_github.yml` |  |
| 101654 | 9 | converted | `rules/linux/resource-development/obtain_capabilities_offensive_python_library_installation.yml` |  |
| 101655 | 7 | converted | `rules/linux/resource-development/obtain_capabilities_offensive_tool_installation_via_package_manager.yml` |  |
| 101656 | 8 | converted | `rules/linux/resource-development/digital_certificates_ssl_tls_certificate_generation.yml` |  |
| 101657 | 8 | converted | `rules/linux/resource-development/software_packing_binary_packing_compilation_tool_detected.yml` |  |
| 101658 | 10 | converted | `rules/correlations/resource_development_multiple_offensive_tool_preparations.yml` |  |
| 101700 | 3 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
| 101701 | 3 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
| 101702 | 3 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
| 101703 | 5 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
| 101705 | 3 | not converted |  | Site application or edge log with a site-specific decoder. Kept private. |
