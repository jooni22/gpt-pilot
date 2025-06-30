# Dokumentacja folderu `core`
## Spis treści
- [core.agents](#core_agents)
- [core.cli](#core_cli)
- [core.config](#core_config)
  - [Klasy](#klasy-core_config)
  - [Funkcje](#funkcje-core_config)
- [core.db](#core_db)
- [core.disk](#core_disk)
- [core.llm](#core_llm)
- [core.log](#core_log)
  - [Funkcje](#funkcje-core_log)
- [core.proc](#core_proc)
- [core.state](#core_state)
- [core.telemetry](#core_telemetry)
  - [Klasy](#klasy-core_telemetry)
- [core.templates](#core_templates)
- [core.ui](#core_ui)
- [core.agents.architect](#core_agents_architect)
  - [Klasy](#klasy-core_agents_architect)
- [core.agents.base](#core_agents_base)
  - [Klasy](#klasy-core_agents_base)
- [core.agents.bug_hunter](#core_agents_bug_hunter)
  - [Klasy](#klasy-core_agents_bug_hunter)
- [core.agents.code_monkey](#core_agents_code_monkey)
  - [Klasy](#klasy-core_agents_code_monkey)
- [core.agents.convo](#core_agents_convo)
  - [Klasy](#klasy-core_agents_convo)
- [core.agents.developer](#core_agents_developer)
  - [Klasy](#klasy-core_agents_developer)
- [core.agents.error_handler](#core_agents_error_handler)
  - [Klasy](#klasy-core_agents_error_handler)
- [core.agents.executor](#core_agents_executor)
  - [Klasy](#klasy-core_agents_executor)
- [core.agents.external_docs](#core_agents_external_docs)
  - [Klasy](#klasy-core_agents_external_docs)
- [core.agents.frontend](#core_agents_frontend)
  - [Klasy](#klasy-core_agents_frontend)
- [core.agents.git](#core_agents_git)
  - [Klasy](#klasy-core_agents_git)
- [core.agents.human_input](#core_agents_human_input)
  - [Klasy](#klasy-core_agents_human_input)
- [core.agents.importer](#core_agents_importer)
  - [Klasy](#klasy-core_agents_importer)
- [core.agents.legacy_handler](#core_agents_legacy_handler)
  - [Klasy](#klasy-core_agents_legacy_handler)
- [core.agents.mixins](#core_agents_mixins)
  - [Klasy](#klasy-core_agents_mixins)
- [core.agents.orchestrator](#core_agents_orchestrator)
  - [Klasy](#klasy-core_agents_orchestrator)
- [core.agents.problem_solver](#core_agents_problem_solver)
  - [Klasy](#klasy-core_agents_problem_solver)
- [core.agents.response](#core_agents_response)
  - [Klasy](#klasy-core_agents_response)
- [core.agents.spec_writer](#core_agents_spec_writer)
  - [Klasy](#klasy-core_agents_spec_writer)
- [core.agents.task_completer](#core_agents_task_completer)
  - [Klasy](#klasy-core_agents_task_completer)
- [core.agents.tech_lead](#core_agents_tech_lead)
  - [Klasy](#klasy-core_agents_tech_lead)
- [core.agents.tech_writer](#core_agents_tech_writer)
  - [Klasy](#klasy-core_agents_tech_writer)
- [core.agents.troubleshooter](#core_agents_troubleshooter)
  - [Klasy](#klasy-core_agents_troubleshooter)
- [core.cli.helpers](#core_cli_helpers)
  - [Funkcje](#funkcje-core_cli_helpers)
- [core.cli.main](#core_cli_main)
  - [Funkcje](#funkcje-core_cli_main)
- [core.config.env_importer](#core_config_env_importer)
  - [Funkcje](#funkcje-core_config_env_importer)
- [core.config.magic_words](#core_config_magic_words)
- [core.config.user_settings](#core_config_user_settings)
  - [Klasy](#klasy-core_config_user_settings)
  - [Funkcje](#funkcje-core_config_user_settings)
- [core.config.version](#core_config_version)
  - [Funkcje](#funkcje-core_config_version)
- [core.db.models](#core_db_models)
- [core.db.session](#core_db_session)
  - [Klasy](#klasy-core_db_session)
- [core.db.setup](#core_db_setup)
  - [Funkcje](#funkcje-core_db_setup)
- [core.db.v0importer](#core_db_v0importer)
  - [Klasy](#klasy-core_db_v0importer)
- [core.disk.ignore](#core_disk_ignore)
  - [Klasy](#klasy-core_disk_ignore)
- [core.disk.vfs](#core_disk_vfs)
  - [Klasy](#klasy-core_disk_vfs)
- [core.llm.anthropic_client](#core_llm_anthropic_client)
  - [Klasy](#klasy-core_llm_anthropic_client)
- [core.llm.azure_client](#core_llm_azure_client)
  - [Klasy](#klasy-core_llm_azure_client)
- [core.llm.base](#core_llm_base)
  - [Klasy](#klasy-core_llm_base)
- [core.llm.convo](#core_llm_convo)
  - [Klasy](#klasy-core_llm_convo)
- [core.llm.groq_client](#core_llm_groq_client)
  - [Klasy](#klasy-core_llm_groq_client)
- [core.llm.openai_client](#core_llm_openai_client)
  - [Klasy](#klasy-core_llm_openai_client)
- [core.llm.parser](#core_llm_parser)
  - [Klasy](#klasy-core_llm_parser)
- [core.llm.prompt](#core_llm_prompt)
  - [Klasy](#klasy-core_llm_prompt)
- [core.llm.request_log](#core_llm_request_log)
  - [Klasy](#klasy-core_llm_request_log)
- [core.proc.exec_log](#core_proc_exec_log)
  - [Klasy](#klasy-core_proc_exec_log)
- [core.proc.process_manager](#core_proc_process_manager)
  - [Klasy](#klasy-core_proc_process_manager)
- [core.state.state_manager](#core_state_state_manager)
  - [Klasy](#klasy-core_state_state_manager)
- [core.templates.base](#core_templates_base)
  - [Klasy](#klasy-core_templates_base)
- [core.templates.example_project](#core_templates_example_project)
- [core.templates.javascript_react](#core_templates_javascript_react)
  - [Klasy](#klasy-core_templates_javascript_react)
- [core.templates.node_express_mongoose](#core_templates_node_express_mongoose)
  - [Klasy](#klasy-core_templates_node_express_mongoose)
- [core.templates.react_express](#core_templates_react_express)
  - [Klasy](#klasy-core_templates_react_express)
- [core.templates.registry](#core_templates_registry)
  - [Klasy](#klasy-core_templates_registry)
- [core.templates.render](#core_templates_render)
  - [Klasy](#klasy-core_templates_render)
  - [Funkcje](#funkcje-core_templates_render)
- [core.templates.vite_react](#core_templates_vite_react)
  - [Klasy](#klasy-core_templates_vite_react)
- [core.ui.base](#core_ui_base)
  - [Klasy](#klasy-core_ui_base)
- [core.ui.console](#core_ui_console)
  - [Klasy](#klasy-core_ui_console)
- [core.ui.ipc_client](#core_ui_ipc_client)
  - [Klasy](#klasy-core_ui_ipc_client)
- [core.ui.ipc_web_broker](#core_ui_ipc_web_broker)
  - [Klasy](#klasy-core_ui_ipc_web_broker)
  - [Funkcje](#funkcje-core_ui_ipc_web_broker)
- [core.ui.run_broker](#core_ui_run_broker)
  - [Funkcje](#funkcje-core_ui_run_broker)
- [core.ui.virtual](#core_ui_virtual)
  - [Klasy](#klasy-core_ui_virtual)
- [core.ui.websocket_ui](#core_ui_websocket_ui)
  - [Klasy](#klasy-core_ui_websocket_ui)
- [core.db.models.base](#core_db_models_base)
  - [Klasy](#klasy-core_db_models_base)
- [core.db.models.branch](#core_db_models_branch)
  - [Klasy](#klasy-core_db_models_branch)
- [core.db.models.exec_log](#core_db_models_exec_log)
  - [Klasy](#klasy-core_db_models_exec_log)
- [core.db.models.file](#core_db_models_file)
  - [Klasy](#klasy-core_db_models_file)
- [core.db.models.file_content](#core_db_models_file_content)
  - [Klasy](#klasy-core_db_models_file_content)
- [core.db.models.llm_request](#core_db_models_llm_request)
  - [Klasy](#klasy-core_db_models_llm_request)
- [core.db.models.project](#core_db_models_project)
  - [Klasy](#klasy-core_db_models_project)
- [core.db.models.project_state](#core_db_models_project_state)
  - [Klasy](#klasy-core_db_models_project_state)
- [core.db.models.specification](#core_db_models_specification)
  - [Klasy](#klasy-core_db_models_specification)
- [core.db.models.user_input](#core_db_models_user_input)
  - [Klasy](#klasy-core_db_models_user_input)

---

---
<a name="core_agents"></a>
## `core.agents`
(Brak docstringu modułu)


---
<a name="core_cli"></a>
## `core.cli`
(Brak docstringu modułu)


---
<a name="core_config"></a>
## `core.config`
(Brak docstringu modułu)

### <a name="klasy-core_config"></a>Klasy
#### `LLMProvider`

    Supported LLM providers.


#### `UIAdapter`

    Supported UI adapters.


#### `ProviderConfig`

    LLM provider configuration.


#### `AgentLLMConfig`

    Configuration for the various LLMs used by Pythagora.

    Each Agent has an LLM provider, from the Enum LLMProvider. If
    AgentLLMConfig is not specified, default will be used.


#### `LLMConfig`

    Complete agent-specific configuration for an LLM.

##### Metody
- `from_provider_and_agent_configs(cls, provider, agent)`: (Brak docstringu)

#### `PromptConfig`

    Configuration for prompt templates:

##### Metody
- `validate_paths(cls, v)`: (Brak docstringu)

#### `LogConfig`

    Configuration for logging.


#### `DBConfig`

    Configuration for database connections.

    Supported URL schemes:

    * sqlite+aiosqlite: SQLite database using the aiosqlite driver

##### Metody
- `validate_url_scheme(cls, v)`: (Brak docstringu)

#### `PlainUIConfig`

    Configuration for plaintext console UI.


#### `LocalIPCConfig`

    Configuration for VSCode extension IPC client.


#### `VirtualUIConfig`

    Configuration for the virtual UI.


#### `FileSystemType`

    Supported filesystem types.


#### `FileSystemConfig`

    Configuration for project workspace.


#### `Config`

    Pythagora Core configuration

##### Metody
- `llm_for_agent(self, agent_name)`:
        Fetch an LLM configuration for a given agent.

        If the agent specific configuration doesn't exist, returns the configuration
        for the 'default' agent.

- `all_llms(self)`:
        Get configuration for all defined LLMs.


#### `ConfigLoader`

    Configuration loader takes care of loading and parsing configuration files.

    The default loader is already initialized as `core.config.loader`. To
    load the configuration from a file, use `core.config.loader.load(path)`.

    To get the current configuration, use `core.config.get_config()`.

##### Metody
- `__init__(self)`: (Brak docstringu)
- `from_json(cls, config)`:
        Parse JSON Into a Config object.

        :param config: JSON string to parse.
        :return: Config object.

- `load(self, path)`:
        Load a configuration from a file.

        :param path: Path to the configuration file.
        :return: Config object.


### <a name="funkcje-core_config"></a>Funkcje
- `adapt_for_bedrock(config)`:
    Adapt the configuration for use with Bedrock.

    :param config: Configuration to adapt.
    :return: Adapted configuration.

- `get_config()`:
    Return current configuration.

    :return: Current configuration object.



---
<a name="core_db"></a>
## `core.db`
(Brak docstringu modułu)


---
<a name="core_disk"></a>
## `core.disk`
(Brak docstringu modułu)


---
<a name="core_llm"></a>
## `core.llm`
(Brak docstringu modułu)


---
<a name="core_log"></a>
## `core.log`
(Brak docstringu modułu)

### <a name="funkcje-core_log"></a>Funkcje
- `setup(config, force)`:
    Set up logging based on the current configuration.

    The method is idempotent unless `force` is set to True,
    in which case it will reconfigure the logging.

- `get_logger(name)`:
    Get log function for a given (module) name

    :return: Logger instance



---
<a name="core_proc"></a>
## `core.proc`
(Brak docstringu modułu)


---
<a name="core_state"></a>
## `core.state`
(Brak docstringu modułu)


---
<a name="core_telemetry"></a>
## `core.telemetry`
(Brak docstringu modułu)

### <a name="klasy-core_telemetry"></a>Klasy
#### `Telemetry`

    Pythagora telemetry data collection.

    This class is a singleton, use the `telemetry` global variable to access it:

    >>> from core.telemetry import telemetry

    To record start of application creation process:

    >>> telemetry.start()

    To record data or increase counters:

    >>> telemetry.set("model", "gpt-4")
    >>> telemetry.inc("num_llm_requests", 5)

    To stop recording and send the data:

    >>> telemetry.stop()
    >>> await telemetry.send()

    Note: all methods are no-ops if telemetry is not enabled.

##### Metody
- `__init__(self)`: (Brak docstringu)
- `clear_data(self)`:
        Reset all telemetry data to default values.

- `clear_counters(self)`:
        Reset telemetry counters while keeping the base data.

- `set(self, name, value)`:
        Set a telemetry data field to a value.

        :param name: name of the telemetry data field
        :param value: value to set the field to

        Note: only known data fields may be set, see `Telemetry.clear_data()` for a list.

- `inc(self, name, value)`:
        Increase a telemetry data field by a value.

        :param name: name of the telemetry data field
        :param value: value to increase the field by (default: 1)

        Note: only known data fields may be increased, see `Telemetry.clear_data()` for a list.

- `start(self)`:
        Record start of application creation process.

- `stop(self)`:
        Record end of application creation process.

- `record_crash(self, exception, end_result)`:
        Record crash diagnostics.

        The formatted stack trace only contains frames from the `core` package
        of gpt-pilot.

        :param exception: exception that caused the crash
        :param end_result: end result of the application (default: "failure")
        :return: formatted stack trace of the exception

        Records the following crash diagnostics data:
        * formatted stack trace
        * exception (class name and message)
        * file:line for the last (innermost) 3 frames of the stack trace, only counting
            the frames from the `core` package.

- `record_llm_request(self, tokens, elapsed_time, is_error)`:
        Record an LLM request.

        :param tokens: number of tokens in the request
        :param elapsed_time: time elapsed for the request
        :param is_error: whether the request resulted in an error

- `calculate_statistics(self)`:
        Calculate statistics for large and slow requests.

- `send(self, event)`:
        Send telemetry data to the phone-home endpoint.

        Note: this method clears all telemetry data after sending it.

- `get_project_stats(self)`: (Brak docstringu)
- `trace_code_event(self, name, data)`:
        Record a code event to trace potential logic bugs.

        :param name: name of the event
        :param data: data to send with the event

- `trace_loop(self, name, task_with_loop)`: (Brak docstringu)


---
<a name="core_templates"></a>
## `core.templates`
(Brak docstringu modułu)


---
<a name="core_ui"></a>
## `core.ui`
(Dokumentacja pakietu)


---
<a name="core_agents_architect"></a>
## `core.agents.architect`
(Brak docstringu modułu)

### <a name="klasy-core_agents_architect"></a>Klasy
#### `AppType`
(Brak docstringu)

#### `SystemDependency`
(Brak docstringu)

#### `PackageDependency`
(Brak docstringu)

#### `Architecture`
(Brak docstringu)

#### `TemplateSelection`
(Brak docstringu)

#### `Architect`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `select_templates(self, spec)`:
        Select project template(s) to use based on the project description.

        Although the Pythagora database models support multiple projects, this
        function will choose at most one project template, as we currently don't
        have templates that could be used together in a single project.

        :param spec: Project specification.
        :return: Dictionary of selected project templates.

- `plan_architecture(self, spec)`: (Brak docstringu)
- `check_compatibility(self, arch)`: (Brak docstringu)
- `prepare_example_project(self, spec)`: (Brak docstringu)
- `check_system_dependencies(self, spec)`:
        Check whether the required system dependencies are installed.

        This also stores the app architecture telemetry data, including the
        information about whether each system dependency is installed.

        :param spec: Project specification.

- `configure_template(self, spec, template_class)`:
        Ask the LLM to configure the template options.

        Based on the project description, the LLM should pick the options that
        make the most sense. If template has no options, the method is a no-op
        and returns an empty options model.

        :param spec: Project specification.
        :param template_class: Template that needs to be configured.
        :return: Configured options model.



---
<a name="core_agents_base"></a>
## `core.agents.base`
(Brak docstringu modułu)

### <a name="klasy-core_agents_base"></a>Klasy
#### `BaseAgent`

    Base class for agents.

##### Metody
- `__init__(self, state_manager, ui)`:
        Create a new agent.

- `current_state(self)`: Current state of the project (read-only).
- `next_state(self)`: Next state of the project (write-only).
- `send_message(self, message, extra_info)`:
        Send a message to the user.

        Convenience method, uses `UIBase.send_message()` to send the message,
        setting the correct source and project state ID.

        :param message: Message to send.
        :param extra_info: Extra information to indicate special functionality in extension

- `ask_question(self, question)`:
        Ask a question to the user and return the response.

        Convenience method, uses `UIBase.ask_question()` to
        ask the question, setting the correct source and project state ID, and
        logging the question/response.

        :param question: Question to ask.
        :param buttons: Buttons to display with the question.
        :param default: Default button to select.
        :param buttons_only: Only display buttons, no text input.
        :param allow_empty: Allow empty input.
        :param full_screen: Show question full screen in extension.
        :param hint: Text to display in a popup as a hint to the question.
        :param verbose: Whether to log the question and response.
        :param initial_text: Initial text input.
        :param extra_info: Extra information to indicate special functionality in extension.
        :param placeholder: Placeholder text for the input field.
        :return: User response.

- `stream_handler(self, content)`:
        Handle streamed response from the LLM.

        Serves as a callback to `AgentBase.llm()` so it can stream the responses to the UI.

        :param content: Response content.

- `error_handler(self, error, message)`:
        Handle error responses from the LLM.

        :param error: The exception that was thrown the the LLM client.
        :param message: Optional message to show.
        :return: Whether the request should be retried.

- `get_llm(self, name, stream_output)`:
        Get a new instance of the agent-specific LLM client.

        The client initializes the UI stream handler and stores the
        request/response to the current state's log. The agent name
        can be overridden in case the agent needs to use a different
        model configuration.

        :param name: Name of the agent for configuration (default: class name).
        :return: LLM client for the agent.

- `run()`:
        Run the agent.

        :return: Response from the agent.



---
<a name="core_agents_bug_hunter"></a>
## `core.agents.bug_hunter`
(Brak docstringu modułu)

### <a name="klasy-core_agents_bug_hunter"></a>Klasy
#### `HuntConclusionType`
(Brak docstringu)

#### `HuntConclusionOptions`
(Brak docstringu)

#### `ImportantLog`
(Brak docstringu)

#### `ImportantLogsForDebugging`
(Brak docstringu)

#### `BugHunter`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `get_bug_reproduction_instructions(self)`: (Brak docstringu)
- `check_logs(self, logs_message)`: (Brak docstringu)
- `ask_user_to_test(self, awaiting_bug_reproduction, awaiting_user_test)`: (Brak docstringu)
- `start_pair_programming(self)`: (Brak docstringu)
- `generate_iteration_convo_so_far(self, omit_last_cycle)`: (Brak docstringu)
- `set_data_for_next_hunting_cycle(self, human_readable_instructions, new_status)`: (Brak docstringu)
- `continue_on(self, convo, button_value, user_response)`: (Brak docstringu)


---
<a name="core_agents_code_monkey"></a>
## `core.agents.code_monkey`
(Brak docstringu modułu)

### <a name="klasy-core_agents_code_monkey"></a>Klasy
#### `Decision`
(Brak docstringu)

#### `Hunk`
(Brak docstringu)

#### `ReviewChanges`
(Brak docstringu)

#### `FileDescription`
(Brak docstringu)

#### `CodeMonkey`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `implement_changes(self, data)`: (Brak docstringu)
- `describe_files(self)`: (Brak docstringu)
- `run_code_review(self, data)`: (Brak docstringu)
- `accept_changes(self, file_path, old_content, new_content)`: (Brak docstringu)
- `review_change(self, file_name, instructions, old_content, new_content)`:
        Review changes that were applied to the file.

        This asks the LLM to act as a PR reviewer and for each part (hunk) of the
        diff, decide if it should be applied (kept) or ignored (removed from the PR).

        :param file_name: name of the file being modified
        :param instructions: instructions for the reviewer
        :param old_content: old file content
        :param new_content: new file content (with proposed changes)
        :return: tuple with file content update with approved changes, and review feedback

        Diff hunk explanation: https://www.gnu.org/software/diffutils/manual/html_node/Hunks.html

- `get_diff_hunks(file_name, old_content, new_content)`:
        Get the diff between two files.

        This uses Python difflib to produce an unified diff, then splits
        it into hunks that will be separately reviewed by the reviewer.

        :param file_name: name of the file being modified
        :param old_content: old file content
        :param new_content: new file content
        :return: change hunks from the unified diff

- `apply_diff(self, file_name, old_content, hunks, fallback)`:
        Apply the diff to the original file content.

        This uses the internal `_apply_patch` method to apply the
        approved diff hunks to the original file content.

        If patch apply fails, the fallback is the full new file content
        with all the changes applied (as if the reviewer approved everythng).

        :param file_name: name of the file being modified
        :param old_content: old file content
        :param hunks: change hunks from the unified diff
        :param fallback: proposed new file content (with all the changes applied)



---
<a name="core_agents_convo"></a>
## `core.agents.convo`
(Brak docstringu modułu)

### <a name="klasy-core_agents_convo"></a>Klasy
#### `AgentConvo`
(Brak docstringu)
##### Metody
- `__init__(self, agent)`: (Brak docstringu)
- `render(self, name, **kwargs)`: (Brak docstringu)
- `template(self, template_name, **kwargs)`: (Brak docstringu)
- `fork(self)`: (Brak docstringu)
- `trim(self, trim_index, trim_count)`:
        Trim the conversation starting from the given index by 1 message.
        :param trim_index:
        :return:

- `require_schema(self, model)`: (Brak docstringu)
- `remove_last_x_messages(self, x)`:
        Remove the last `x` messages from the conversation.



---
<a name="core_agents_developer"></a>
## `core.agents.developer`
(Brak docstringu modułu)

### <a name="klasy-core_agents_developer"></a>Klasy
#### `StepType`
(Brak docstringu)

#### `CommandOptions`
(Brak docstringu)

#### `SaveFileOptions`
(Brak docstringu)

#### `SaveFileStep`
(Brak docstringu)

#### `CommandStep`
(Brak docstringu)

#### `HumanInterventionStep`
(Brak docstringu)

#### `UtilityFunction`
(Brak docstringu)

#### `TaskSteps`
(Brak docstringu)

#### `Developer`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `breakdown_current_iteration(self)`:
        Breaks down current iteration or task review into steps.

        :return: AgentResponse.done(self) when the breakdown is done

- `breakdown_current_task(self)`: (Brak docstringu)
- `set_next_steps(self, response, source)`: (Brak docstringu)
- `remove_duplicate_steps(self, data)`: (Brak docstringu)
- `ask_to_execute_task(self)`:
        Asks the user to approve, skip or edit the current task.

        If task is edited, the method returns False so that the changes are saved. The
        Orchestrator will rerun the agent on the next iteration.

        :return: True if the task should be executed as is, False if the task is skipped or edited

- `update_knowledge_base(self)`:
        Update the knowledge base with the current task and steps.



---
<a name="core_agents_error_handler"></a>
## `core.agents.error_handler`
(Brak docstringu modułu)

### <a name="klasy-core_agents_error_handler"></a>Klasy
#### `ErrorHandler`

    Error handler agent.

    Error handler is responsible for handling errors returned by other agents. If it's possible
    to recover from the error, it should do it (which may include updating the "next" state) and
    return DONE. Otherwise it should return EXIT to tell Orchestrator to quit the application.

##### Metody
- `run(self)`: (Brak docstringu)
- `handle_command_error(self, message, details)`:
        Handle an error returned by Executor agent.

        Error message must be the analyis of the command execution, and the details must contain:
        * cmd - command that was executed
        * timeout - timeout for the command if any (or None if no timeout was used)
        * status_code - exit code for the command (or None if the command timed out)
        * stdout - standard output of the command
        * stderr - standard error of the command

        :return: AgentResponse



---
<a name="core_agents_executor"></a>
## `core.agents.executor`
(Brak docstringu modułu)

### <a name="klasy-core_agents_executor"></a>Klasy
#### `CommandResult`

    Analysis of the command run and decision on the next steps.


#### `Executor`
(Brak docstringu)
##### Metody
- `__init__(self, state_manager, ui)`:
        Create a new Executor agent

- `for_step(self, step)`: (Brak docstringu)
- `output_handler(self, out, err)`: (Brak docstringu)
- `exit_handler(self, process)`: (Brak docstringu)
- `run(self)`: (Brak docstringu)
- `check_command_output(self, cmd, timeout, stdout, stderr, status_code)`: (Brak docstringu)
- `complete(self)`:
        Mark the step as complete.

        Note that this marks the step complete in the next state. If there's an error,
        the state won't get committed and the error handler will have access to the
        current state, where this step is still unfinished.

        This is intentional, so that the error handler can decide what to do with the
        information we give it.



---
<a name="core_agents_external_docs"></a>
## `core.agents.external_docs`
(Brak docstringu modułu)

### <a name="klasy-core_agents_external_docs"></a>Klasy
#### `DocQueries`
(Brak docstringu)

#### `SelectedDocsets`
(Brak docstringu)

#### `ExternalDocumentation`
Agent in charge of collecting and storing additional documentation.

    Docs are per task and are stores in the `docs` variable in the project state.
    This agent ensures documentation is collected only once per task.

    Agent does 2 LLM interactions:
        1. Ask the LLM to select useful documentation from a predefined list.
        2. Ask the LLM to come up with a query to use to fetch the actual documentation snippets.

    Agent does 2 calls to our documentation API:
        1. Fetch all the available docsets. `docset` is a collection of documentation snippets
           for a single topic, eg. VueJS API Reference docs.
        2. Fetch the documentation snippets for given queries.


##### Metody
- `run(self)`: (Brak docstringu)


---
<a name="core_agents_frontend"></a>
## `core.agents.frontend`
(Brak docstringu modułu)

### <a name="klasy-core_agents_frontend"></a>Klasy
#### `Frontend`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `init_frontend(self)`:
        Builds frontend of the app.

        :return: AgentResponse.done(self)

- `start_frontend(self)`:
        Starts the frontend of the app.

- `continue_frontend(self)`:
        Continues building the frontend of the app after the initial user input.

- `iterate_frontend(self)`:
        Iterates over the frontend.

        :return: True if the frontend is fully built, False otherwise.

- `end_frontend_iteration(self, finished)`:
        Ends the frontend iteration.

        :param finished: Whether the frontend is fully built.
        :return: AgentResponse.done(self)

- `process_response(self, response_blocks)`:
        Processes the response blocks from the LLM.

        :param response_blocks: The response blocks from the LLM.
        :return: AgentResponse.done(self)

- `apply_template(self, options)`:
        Applies a template to the frontend.

- `set_app_details(self)`:
        Sets the app details.



---
<a name="core_agents_git"></a>
## `core.agents.git`
(Brak docstringu modułu)

### <a name="klasy-core_agents_git"></a>Klasy
#### `GitMixin`

    Mixin class for git commands

##### Metody
- `check_git_installed(self)`: Check if git is installed on the system.
- `is_git_initialized(self)`: Check if git is initialized in the workspace.
- `init_git_if_needed(self)`:
        Initialize git repository if it hasn't been initialized yet.
        Returns True if initialization was needed and successful.

- `git_commit(self)`:
        Create a git commit with the specified message.
        Raises RuntimeError if the commit fails.



---
<a name="core_agents_human_input"></a>
## `core.agents.human_input`
(Brak docstringu modułu)

### <a name="klasy-core_agents_human_input"></a>Klasy
#### `HumanInput`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `human_intervention(self, step)`: (Brak docstringu)
- `input_required(self, files)`: (Brak docstringu)


---
<a name="core_agents_importer"></a>
## `core.agents.importer`
(Brak docstringu modułu)

### <a name="klasy-core_agents_importer"></a>Klasy
#### `Importer`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `start_import_process(self)`: (Brak docstringu)
- `analyze_project(self)`: (Brak docstringu)


---
<a name="core_agents_legacy_handler"></a>
## `core.agents.legacy_handler`
(Brak docstringu modułu)

### <a name="klasy-core_agents_legacy_handler"></a>Klasy
#### `LegacyHandler`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)


---
<a name="core_agents_mixins"></a>
## `core.agents.mixins`
(Brak docstringu modułu)

### <a name="klasy-core_agents_mixins"></a>Klasy
#### `ReadFilesAction`
(Brak docstringu)

#### `AddFilesAction`
(Brak docstringu)

#### `RemoveFilesAction`
(Brak docstringu)

#### `DoneBooleanAction`
(Brak docstringu)

#### `RelevantFiles`
(Brak docstringu)

#### `Test`
(Brak docstringu)

#### `TestSteps`
(Brak docstringu)

#### `ChatWithBreakdownMixin`

    Provides a method to chat with the user and provide a breakdown of the conversation.

##### Metody
- `chat_with_breakdown(self, convo, breakdown)`:
        Chat with the user and provide a breakdown of the conversation.

        :param convo: The conversation object.
        :param breakdown: The breakdown of the conversation.
        :return: The breakdown.


#### `IterationPromptMixin`

    Provides a method to find a solution to a problem based on user feedback.

    Used by ProblemSolver and Troubleshooter agents.

##### Metody
- `find_solution(self, user_feedback)`:
        Generate a new solution for the problem the user reported.

        :param user_feedback: User feedback about the problem.
        :param user_feedback_qa: Additional q/a about the problem provided by the user (optional).
        :param next_solution_to_try: Hint from ProblemSolver on which solution to try (optional).
        :param bug_hunting_cycles: Data about logs that need to be added to the code (optional).
        :return: The generated solution to the problem.


#### `RelevantFilesMixin`

    Provides a method to get relevant files for the current task.

##### Metody
- `get_relevant_files(self, user_feedback, solution_description)`: (Brak docstringu)

#### `FileDiffMixin`

    Provides a method to generate a diff between two files.

##### Metody
- `get_line_changes(self, old_content, new_content)`:
        Get the number of added and deleted lines between two files.

        This uses Python difflib to produce a unified diff, then counts
        the number of added and deleted lines.

        :param old_content: old file content
        :param new_content: new file content
        :return: a tuple (added_lines, deleted_lines)



---
<a name="core_agents_orchestrator"></a>
## `core.agents.orchestrator`
(Brak docstringu modułu)

### <a name="klasy-core_agents_orchestrator"></a>Klasy
#### `Orchestrator`

    Main agent that controls the flow of the process.

    Based on the current state of the project, the orchestrator invokes
    all other agents. It is also responsible for determining when each
    step is done and the project state needs to be committed to the database.

##### Metody
- `run(self)`:
        Run the Orchestrator agent.

        :return: True if the Orchestrator exited successfully, False otherwise.

- `install_dependencies(self)`: (Brak docstringu)
- `handle_parallel_responses(self, agent, responses)`:
        Handle responses from agents that were run in parallel.

        This method is called when multiple agents are run in parallel, and it
        should return a single response that represents the combined responses
        of all agents.

        :param agent: The original agent that was run in parallel.
        :param responses: List of responses from all agents.
        :return: Combined response.

- `offline_changes_check(self)`:
        Check for changes outside Pythagora.

        If there are changes, ask the user if they want to keep them, and
        import if needed.

- `handle_done(self, agent, response)`:
        Handle the DONE response from the agent and commit current state to the database.

        This also checks for any files created or modified outside Pythagora and
        imports them. If any of the files require input from the user, the returned response
        will trigger the HumanInput agent to ask the user to provide the required input.


- `create_agent(self, prev_response)`: (Brak docstringu)
- `create_agent_for_step(self, step)`: (Brak docstringu)
- `import_files(self)`: (Brak docstringu)
- `init_ui(self)`: (Brak docstringu)
- `update_stats(self)`: (Brak docstringu)


---
<a name="core_agents_problem_solver"></a>
## `core.agents.problem_solver`
(Brak docstringu modułu)

### <a name="klasy-core_agents_problem_solver"></a>Klasy
#### `AlternativeSolutions`
(Brak docstringu)

#### `ProblemSolver`
(Brak docstringu)
##### Metody
- `__init__(self, *args, **kwargs)`: (Brak docstringu)
- `run(self)`: (Brak docstringu)
- `generate_alternative_solutions(self)`: (Brak docstringu)
- `try_alternative_solutions(self)`: (Brak docstringu)
- `ask_for_preferred_solution(self)`: (Brak docstringu)


---
<a name="core_agents_response"></a>
## `core.agents.response`
(Brak docstringu modułu)

### <a name="klasy-core_agents_response"></a>Klasy
#### `ResponseType`
(Brak docstringu)

#### `AgentResponse`
(Brak docstringu)
##### Metody
- `__init__(self, type, agent, data)`: (Brak docstringu)
- `__repr__(self)`: (Brak docstringu)
- `done(agent)`: (Brak docstringu)
- `error(agent, message, details)`: (Brak docstringu)
- `cancel(agent)`: (Brak docstringu)
- `exit(agent)`: (Brak docstringu)
- `describe_files(agent)`: (Brak docstringu)
- `input_required(agent, files)`: (Brak docstringu)
- `import_project(agent)`: (Brak docstringu)
- `external_docs_required(agent)`: (Brak docstringu)
- `update_specification(agent, description)`: (Brak docstringu)


---
<a name="core_agents_spec_writer"></a>
## `core.agents.spec_writer`
(Brak docstringu modułu)

### <a name="klasy-core_agents_spec_writer"></a>Klasy
#### `SpecWriter`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `initialize_spec(self)`: (Brak docstringu)
- `update_spec(self, iteration_mode)`: (Brak docstringu)
- `check_prompt_complexity(self, prompt)`: (Brak docstringu)
- `analyze_spec(self, spec)`: (Brak docstringu)
- `review_spec(self, desc, spec)`: (Brak docstringu)


---
<a name="core_agents_task_completer"></a>
## `core.agents.task_completer`
(Brak docstringu modułu)

### <a name="klasy-core_agents_task_completer"></a>Klasy
#### `TaskCompleter`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)


---
<a name="core_agents_tech_lead"></a>
## `core.agents.tech_lead`
(Brak docstringu modułu)

### <a name="klasy-core_agents_tech_lead"></a>Klasy
#### `APIEndpoint`
(Brak docstringu)

#### `Epic`
(Brak docstringu)

#### `Task`
(Brak docstringu)

#### `DevelopmentPlan`
(Brak docstringu)

#### `EpicPlan`
(Brak docstringu)

#### `TechLead`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `create_initial_project_epic(self)`: (Brak docstringu)
- `apply_project_templates(self)`: (Brak docstringu)
- `ask_for_new_feature(self)`: (Brak docstringu)
- `plan_epic(self, epic)`: (Brak docstringu)
- `update_epics_and_tasks(self, edited_plan_string)`: (Brak docstringu)


---
<a name="core_agents_tech_writer"></a>
## `core.agents.tech_writer`
(Brak docstringu modułu)

### <a name="klasy-core_agents_tech_writer"></a>Klasy
#### `TechnicalWriter`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `send_congratulations(self)`: (Brak docstringu)
- `create_readme(self)`: (Brak docstringu)


---
<a name="core_agents_troubleshooter"></a>
## `core.agents.troubleshooter`
(Brak docstringu modułu)

### <a name="klasy-core_agents_troubleshooter"></a>Klasy
#### `BugReportQuestions`
(Brak docstringu)

#### `RouteFilePaths`
(Brak docstringu)

#### `Troubleshooter`
(Brak docstringu)
##### Metody
- `run(self)`: (Brak docstringu)
- `propose_solution(self)`: (Brak docstringu)
- `create_iteration(self)`: (Brak docstringu)
- `complete_task(self)`:
        No more coding or user interaction needed for the current task, mark it as reviewed.
        After this it goes to TechnicalWriter for documentation.

- `get_run_command(self)`: (Brak docstringu)
- `get_user_instructions(self)`: (Brak docstringu)
- `get_user_feedback(self, run_command, user_instructions, last_iteration)`:
        Ask the user to test the app and provide feedback.

        :return (bool, bool, str): Tuple containing "should_iterate", "is_loop" and
        "user_feedback" respectively.

        If "should_iterate" is False, the user has confirmed that the app works as expected and there's
        nothing for the troubleshooter or problem solver to do.

        If "is_loop" is True, Pythagora is stuck in a loop and needs to consider alternative solutions.

        The last element in the tuple is the user feedback, which may be empty if the user provided no
        feedback (eg. if they just clicked on "Continue" or "Start Pair Programming").

- `try_next_alternative_solution(self, user_feedback, user_feedback_qa)`:
        Call the ProblemSolver to try an alternative solution.

        Stores the user feedback and sets iteration state so that ProblemSolver will be triggered.

        :param user_feedback: User feedback to store in the iteration state.
        :param user_feedback_qa: Additional questions/answers about the problem.
        :return: Agent response done.

- `generate_bug_report(self, run_command, user_instructions, user_feedback)`:
        Generate a bug report from the user feedback.

        :param run_command: The command to run to test the app.
        :param user_instructions: Instructions on how to test the functionality.
        :param user_feedback: The user feedback.
        :return: Additional questions and answers to generate a better bug report.

- `trace_loop(self, trace_event)`: (Brak docstringu)


---
<a name="core_cli_helpers"></a>
## `core.cli.helpers`
(Brak docstringu modułu)

### <a name="funkcje-core_cli_helpers"></a>Funkcje
- `parse_llm_endpoint(value)`:
    Parse --llm-endpoint command-line option.

    Option syntax is: --llm-endpoint <provider>:<url>

    :param value: Argument value.
    :return: Tuple with LLM provider and URL, or None if the option wasn't provided.

- `parse_llm_key(value)`:
    Parse --llm-key command-line option.

    Option syntax is: --llm-key <provider>:<key>

    :param value: Argument value.
    :return: Tuple with LLM provider and key, or None if if the option wasn't provided.

- `parse_arguments()`:
    Parse command-line arguments.

    Available arguments:
        --help: Show the help message
        --config: Path to the configuration file
        --show-config: Output the default configuration to stdout
        --default-config: Output the configuration to stdout
        --level: Log level (debug,info,warning,error,critical)
        --database: Database URL
        --local-ipc-port: Local IPC port to connect to
        --local-ipc-host: Local IPC host to connect to
        --version: Show the version and exit
        --list: List all projects
        --list-json: List all projects in JSON format
        --project: Load a specific project
        --branch: Load a specific branch
        --step: Load a specific step in a project/branch
        --llm-endpoint: Use specific API endpoint for the given provider
        --llm-key: Use specific LLM key for the given provider
        --import-v0: Import data from a v0 (gpt-pilot) database with the given path
        --email: User's email address, if provided
        --extension-version: Version of the VSCode extension, if used
        --no-check: Disable initial LLM API check
        --use-git: Use Git for version control
    :return: Parsed arguments object.

- `load_config(args)`:
    Load Pythagora JSON configuration file and apply command-line arguments.

    :param args: Command-line arguments (at least `config` must be present).
    :return: Configuration object, or None if config couldn't be loaded.

- `list_projects_json(db)`:
    List all projects in the database in JSON format.

- `list_projects(db)`:
    List all projects in the database.

- `load_project(sm, project_id, branch_id, step_index)`:
    Load a project from the database.

    :param sm: State manager.
    :param project_id: Project ID (optional, loads the last step in the main branch).
    :param branch_id: Branch ID (optional, loads the last step in the branch).
    :param step_index: Step index (optional, loads the state at the given step).
    :return: True if the project was loaded successfully, False otherwise.

- `delete_project(db, project_id)`:
    Delete a project from a database.

    :param sm: State manager.
    :param project_id: Project ID.
    :return: True if project was deleted, False otherwise.

- `show_config()`:
    Print the current configuration to stdout.

- `init()`:
    Initialize the application.

    Loads configuration, sets up logging and UI, initializes the database
    and runs database migrations.

    :return: Tuple with UI, db session manager, file manager, and command-line arguments.



---
<a name="core_cli_main"></a>
## `core.cli.main`
(Brak docstringu modułu)

### <a name="funkcje-core_cli_main"></a>Funkcje
- `cleanup(ui)`: (Brak docstringu)
- `run_project(sm, ui, args)`:
    Work on the project.

    Starts the orchestrator agent with the newly loaded/created project
    and runs it until the orchestrator decides to exit.

    :param sm: State manager.
    :param ui: User interface.
    :param args: Command-line arguments.
    :return: True if the orchestrator exited successfully, False otherwise.

- `llm_api_check(ui)`:
    Check whether the configured LLMs are reachable in parallel.

    :param ui: UI we'll use to report any issues
    :return: True if all the LLMs are reachable.

- `start_new_project(sm, ui)`:
    Start a new project.

    :param sm: State manager.
    :param ui: User interface.
    :return: True if the project was created successfully, False otherwise.

- `run_pythagora_session(sm, ui, args)`:
    Run a Pythagora session.

    :param sm: State manager.
    :param ui: User interface.
    :param args: Command-line arguments.
    :return: True if the application ran successfully, False otherwise.

- `async_main(ui, db, args)`:
    Main application coroutine.

    :param ui: User interface.
    :param db: Database session manager.
    :param args: Command-line arguments.
    :return: True if the application ran successfully, False otherwise.

- `run_pythagora()`: (Brak docstringu)


---
<a name="core_config_env_importer"></a>
## `core.config.env_importer`
(Brak docstringu modułu)

### <a name="funkcje-core_config_env_importer"></a>Funkcje
- `import_from_dotenv(new_config_path)`:
    Import configuration from old gpt-pilot .env file and save it to a new format.

    If the configuration is already loaded, does nothing. If the target file
    already exists, it's parsed as is (it's not overwritten).

    Otherwise, loads the values from `pilot/.env` file and creates a new configuration
    with the relevant settings.

    This intentionally DOES NOT load the .env variables into the current process
    environments, to avoid polluting it with old settings.

    :param new_config_path: Path to save the new configuration file.
    :return: True if the configuration was imported, False otherwise.

- `convert_config(values)`: (Brak docstringu)


---
<a name="core_config_magic_words"></a>
## `core.config.magic_words`
(Brak docstringu modułu)


---
<a name="core_config_user_settings"></a>
## `core.config.user_settings`
(Brak docstringu modułu)

### <a name="klasy-core_config_user_settings"></a>Klasy
#### `TelemetrySettings`
(Brak docstringu)

#### `UserSettings`

    This object holds all the global user settings, that are applicable for
    all Pythagora/GPT-Pilot installations.

    The use settings are stored in a JSON file in the config directory.

    The config directory is determined by the following rules:
    * If the XDG_CONFIG_HOME environment variable is set (desktop Linux), use that.
    * If the APPDATA environment variable is set (Windows), use that.
    * Otherwise, use the POSIX default ~/.<app-name> (MacOS, server Linux).

    This is a singleton object, use it by importing the instance directly
    from the module:

    >>> from config.user_settings import settings
    >>> print(settings.telemetry.id)
    >>> print(settings.config_path)

##### Metody
- `load()`: (Brak docstringu)
- `save(self)`: (Brak docstringu)
- `config_path(self)`: (Brak docstringu)

### <a name="funkcje-core_config_user_settings"></a>Funkcje
- `resolve_config_dir()`:
    Figure out where to store the global config file(s).

    :return: path to the desired location config directory

    See the UserSettings docstring for details on how the config directory is
    determined.



---
<a name="core_config_version"></a>
## `core.config.version`
(Brak docstringu modułu)

### <a name="funkcje-core_config_version"></a>Funkcje
- `get_git_commit()`:
    Return the current git commit (if running from a repo).

    :return: commit hash or None if not running from a git repo

- `get_package_version()`:
    Get package version as defined pyproject.toml.

    If not found, returns "0.0.0."

    :return: package version as defined in pyproject.toml

- `get_version()`:
    Find and return the current version of Pythagora Core.

    The version string is built from the package version and the current
    git commit hash (if running from a git repo).

    Example: 0.0.0-gitbf01c19

    :return: version string



---
<a name="core_db_models"></a>
## `core.db.models`
(Brak docstringu modułu)


---
<a name="core_db_session"></a>
## `core.db.session`
(Brak docstringu modułu)

### <a name="klasy-core_db_session"></a>Klasy
#### `SessionManager`

    Async-aware context manager for database session.

    Usage:

    >>> config = DBConfig(url="sqlite+aiosqlite:///test.db")
    >>> async with DBSession(config) as session:
    ...     # Do something with the session

##### Metody
- `__init__(self, config)`:
        Initialize the session manager with the given configuration.

        :param config: Database configuration.

- `start(self)`: (Brak docstringu)
- `close(self)`: (Brak docstringu)
- `__aenter__(self)`: (Brak docstringu)
- `__aexit__(self, exc_type, exc_val, exc_tb)`: (Brak docstringu)


---
<a name="core_db_setup"></a>
## `core.db.setup`
(Brak docstringu modułu)

### <a name="funkcje-core_db_setup"></a>Funkcje
- `run_migrations(config)`:
    Run database migrations using Alembic.

    This needs to happen synchronously, before the asyncio
    mainloop is started, and before any database access.

    :param config: Database configuration.



---
<a name="core_db_v0importer"></a>
## `core.db.v0importer`
(Brak docstringu modułu)

### <a name="klasy-core_db_v0importer"></a>Klasy
#### `ImporterStateManager`
(Brak docstringu)
##### Metody
- `init_file_system(self, load_existing)`:
        Initialize in-memory file system.

        We don't want to overwrite all the files on disk while importing
        the legacy database, as this could overwrite new changes that the
        user might have done in the meantime. Project loading will handle that.


#### `LegacyDatabaseImporter`
(Brak docstringu)
##### Metody
- `__init__(self, session_manager, dbpath)`: (Brak docstringu)
- `import_database(self)`: (Brak docstringu)
- `load_legacy_database(self)`: (Brak docstringu)
- `verify_schema(self)`: (Brak docstringu)
- `get_apps(self)`: (Brak docstringu)
- `get_app_info(self, app_id)`: (Brak docstringu)
- `get_task_info(self, dev_step_id, prompt_data_json, llm_response)`: (Brak docstringu)
- `get_task_files(self, dev_step_id)`: (Brak docstringu)
- `save_to_new_database(self, info)`:
        Save projects to the new database

        :param info: A dictionary with app_id as key and app info as value.
        :return: Number of projects saved to the new database.

- `save_app(self, app_id, app_info)`: (Brak docstringu)
- `save_latest_task(self, task)`: (Brak docstringu)
- `save_task_files(self, files)`: (Brak docstringu)


---
<a name="core_disk_ignore"></a>
## `core.disk.ignore`
(Brak docstringu modułu)

### <a name="klasy-core_disk_ignore"></a>Klasy
#### `IgnoreMatcher`

    A class to match paths against a list of ignore patterns or
    file attributes (size, type).

##### Metody
- `__init__(self, root_path, ignore_paths)`:
        Initialize the IgnoreMatcher object.

        Ignore paths are matched agains the file name and the full path,
        and may include shell-like wildcards ("*" for any number of characters,
        "?" for a single character). Paths are normalized, so "/" works on both
        Unix and Windows, and Windows matching is case insensitive.

        :param root_path: Root path to use when checking files on disk.
        :param ignore_paths: List of patterns to ignore.
        :param ignore_size_threshold: Files larger than this size will be ignored.

- `ignore(self, path)`:
        Check if the given path matches any of the ignore patterns.

        :param path: (Relative) path to the file or directory to check
        :return: True if the path matches any of the ignore patterns, False otherwise



---
<a name="core_disk_vfs"></a>
## `core.disk.vfs`
(Brak docstringu modułu)

### <a name="klasy-core_disk_vfs"></a>Klasy
#### `VirtualFileSystem`
(Brak docstringu)
##### Metody
- `save(self, path, content)`:
        Save content to a file. Use for both new and updated files.

        :param path: Path to the file, relative to project root.
        :param content: Content to save.

- `read(self, path)`:
        Read file contents.

        :param path: Path to the file, relative to project root.
        :return: File contents.

- `remove(self, path)`:
        Remove a file.

        If file doesn't exist or is a directory, or if the file is ignored,
        do nothing.

        :param path: Path to the file, relative to project root.

- `get_full_path(self, path)`:
        Get the full path to a file.

        This should be used to check the full path of the file on whichever
        file system it locally is stored. For example, getting a full path
        to a file and then passing it to an external program via run_command
        should work.

        :param path: Path to the file, relative to project root.
        :return: Full path to the file.

- `list(self, prefix)`:
        Return a list of files in the project.

        File paths are relative to the project root.

        :param prefix: Optional prefix to filter files for.
        :return: List of file paths.

- `hash(self, path)`: (Brak docstringu)
- `hash_string(content)`: (Brak docstringu)

#### `MemoryVFS`
(Brak docstringu)
##### Metody
- `__init__(self)`: (Brak docstringu)
- `save(self, path, content)`: (Brak docstringu)
- `read(self, path)`: (Brak docstringu)
- `remove(self, path)`: (Brak docstringu)
- `get_full_path(self, path)`: (Brak docstringu)

#### `LocalDiskVFS`
(Brak docstringu)
##### Metody
- `__init__(self, root, create, allow_existing, ignore_matcher)`: (Brak docstringu)
- `get_full_path(self, path)`: (Brak docstringu)
- `save(self, path, content)`: (Brak docstringu)
- `read(self, path)`: (Brak docstringu)
- `remove(self, path)`: (Brak docstringu)


---
<a name="core_llm_anthropic_client"></a>
## `core.llm.anthropic_client`
(Brak docstringu modułu)

### <a name="klasy-core_llm_anthropic_client"></a>Klasy
#### `CustomAssertionError`
(Brak docstringu)

#### `AnthropicClient`
(Brak docstringu)
##### Metody
- `rate_limit_sleep(self, err)`:
        Anthropic rate limits docs:
        https://docs.anthropic.com/en/api/rate-limits#response-headers
        Limit reset times are in RFC 3339 format.




---
<a name="core_llm_azure_client"></a>
## `core.llm.azure_client`
(Brak docstringu modułu)

### <a name="klasy-core_llm_azure_client"></a>Klasy
#### `AzureClient`
(Brak docstringu)


---
<a name="core_llm_base"></a>
## `core.llm.base`
(Brak docstringu modułu)

### <a name="klasy-core_llm_base"></a>Klasy
#### `LLMError`
(Brak docstringu)

#### `APIError`
(Brak docstringu)
##### Metody
- `__init__(self, message)`: (Brak docstringu)

#### `BaseLLMClient`

    Base asynchronous streaming client for language models.

    Example usage:

    >>> async def stream_handler(content: str):
    ...     print(content)
    ...
    >>> def parser(content: str) -> dict:
    ...     return json.loads(content)
    ...
    >>> client_class = BaseClient.for_provider(provider)
    >>> client = client_class(config, stream_handler=stream_handler)
    >>> response, request_log = await client(convo, parser=parser)

##### Metody
- `__init__(self, config)`:
        Initialize the client with the given configuration.

        :param config: Configuration for the client.
        :param stream_handler: Optional handler for streamed responses.

- `__call__(self, convo)`:
        Invoke the LLM with the given conversation.

        Stream handler, if provided, should be an async function
        that takes a single argument, the response content (str).
        It will be called for each response chunk.

        Parser, if provided, should be a function that takes the
        response content (str) and returns the parsed response.
        On parse error, the parser should raise a ValueError with
        a descriptive error message that will be sent back to the LLM
        to retry, up to max_retries.

        :param convo: Conversation to send to the LLM.
        :param parser: Optional parser for the response.
        :param max_retries: Maximum number of retries for parsing the response.
        :param json_mode: If True, the response is expected to be JSON.
        :return: Tuple of the (parsed) response and request log entry.

- `api_check(self)`:
        Perform an LLM API check.

        :return: True if the check was successful, False otherwise.

- `for_provider(provider)`:
        Return LLM client for the specified provider.

        :param provider: Provider to return the client for.
        :return: Client class for the specified provider.

- `rate_limit_sleep(self, err)`:
        Return how long we need to sleep because of rate limiting.

        These are computed from the response headers that each LLM returns.
        For details, check the implementation for the specific LLM. If there
        are no rate limiting headers, we assume that the request should not
        be retried and return None (this will be the case for insufficient
        quota/funds in the account).

        :param err: RateLimitError that was raised by the LLM client.
        :return: optional timedelta to wait before trying again



---
<a name="core_llm_convo"></a>
## `core.llm.convo`
(Brak docstringu modułu)

### <a name="klasy-core_llm_convo"></a>Klasy
#### `Convo`

    A conversation between a user and a Large Language Model (LLM) assistant.

    Holds messages and an optional metadata log (list of dicts with
    prompt information).

##### Metody
- `__init__(self, content)`:
        Initialize a new conversation.

        :param content: Initial system message (optional).

- `add(self, role, content, name)`:
        Add a message to the conversation.

        In most cases, you should use the convenience methods instead.

        :param role: Role of the message (system, user, assistant, function).
        :param content: Content of the message.
        :param name: Name of the message sender (optional).
        :return: The conv object.

- `system(self, content, name)`:
        Add a system message to the conversation.

        System messages can use `name` for showing example conversations
        between an example user and an example assistant.

        :param content: Content of the message.
        :param name: Name of the message sender (optional).
        :return: The convo object.

- `user(self, content, name)`:
        Add a user message to the conversation.

        :param content: Content of the message.
        :param name: User name (optional).
        :return: The convo object.

- `assistant(self, content, name)`:
        Add an assistant message to the conversation.

        :param content: Content of the message.
        :param name: Assistant name (optional).
        :return: The convo object.

- `function(self, content, name)`:
        Add a function (tool) response to the conversation.

        :param content: Content of the message.
        :param name: Function/tool name (optional).
        :return: The convo object.

- `fork(self)`:
        Create an identical copy of the conversation.

        This performs a deep copy of all the message
        contents, so you can safely modify both the
        parent and the child conversation.

        :return: A copy of the conversation.

- `after(self, parent)`:
        Create a chat with only messages after the last common
        message (that appears in both parent conversation and
        this one).

        :param parent: Parent conversation.
        :return: A new conversation with only new messages.

- `last(self)`:
        Get the last message in the conversation.

        :return: The last message, or None if the conversation is empty.

- `__iter__(self)`:
        Iterate over the messages in the conversation.

        :return: An iterator over the messages.

- `__repr__(self)`: (Brak docstringu)
- `truncate(self, max_tokens)`:
        Truncate the conversation to fit within the token limit.

        This method removes messages from the middle of the conversation
        until the total token count is below the specified limit.

        :param max_tokens: Maximum number of tokens allowed.



---
<a name="core_llm_groq_client"></a>
## `core.llm.groq_client`
(Brak docstringu modułu)

### <a name="klasy-core_llm_groq_client"></a>Klasy
#### `GroqClient`
(Brak docstringu)
##### Metody
- `rate_limit_sleep(self, err)`:
        Groq rate limits docs: https://console.groq.com/docs/rate-limits

        Groq includes `retry-after` header when 429 RateLimitError is
        thrown, so we use that instead of calculating our own backoff time.



---
<a name="core_llm_openai_client"></a>
## `core.llm.openai_client`
(Brak docstringu modułu)

### <a name="klasy-core_llm_openai_client"></a>Klasy
#### `OpenAIClient`
(Brak docstringu)
##### Metody
- `rate_limit_sleep(self, err)`:
        OpenAI rate limits docs:
        https://platform.openai.com/docs/guides/rate-limits/error-mitigation
        Limit reset times are in "2h32m54s" format.



---
<a name="core_llm_parser"></a>
## `core.llm.parser`
(Brak docstringu modułu)

### <a name="klasy-core_llm_parser"></a>Klasy
#### `CodeBlock`
(Brak docstringu)

#### `ParsedBlocks`
(Brak docstringu)

#### `DescriptiveCodeBlockParser`

    Parse Markdown code blocks with their descriptions from a string.
    Returns both the original response and structured data about each block.

    Each block entry contains:
    - description: The text line immediately preceding the code block
    - content: The actual content of the code block

    Example usage:
    >>> parser = DescriptiveCodeBlockParser()
    >>> text = '''file: next.config.js
    ... ```js
    ... module.exports = {
    ...   reactStrictMode: true,
    ... };
    ... ```'''
    >>> result = parser(text)
    >>> assert result.blocks[0].description == "file: next.config.js"

##### Metody
- `__init__(self)`: (Brak docstringu)
- `__call__(self, text)`: (Brak docstringu)

#### `MultiCodeBlockParser`

    Parse multiple Markdown code blocks from a string.

    Expects zero or more blocks, and ignores any text
    outside of the code blocks.

    Example usage:

    >>> parser = MultiCodeBlockParser()
    >>> text = '''
    ... text outside block
    ...
    ... ```python
    ... first block
    ... ```
    ... some text between blocks
    ... ```js
    ... more
    ... code
    ... ```
    ... some text after blocks
    '''
    >>> assert parser(text) == ["first block", "more
code"]

    If no code blocks are found, an empty list is returned:

##### Metody
- `__init__(self)`: (Brak docstringu)
- `__call__(self, text)`: (Brak docstringu)

#### `CodeBlockParser`

    Parse a Markdown code block from a string.

    Expects exactly one code block, and ignores
    any text before or after it.

    Usage:
    >>> parser = CodeBlockParser()
    >>> text = "text
```py
codeblock
'''
more text"
    >>> assert parser(text) == "codeblock"

    This is a special case of MultiCodeBlockParser,
    checking that there's exactly one block.

##### Metody
- `__call__(self, text)`: (Brak docstringu)

#### `OptionalCodeBlockParser`
(Brak docstringu)
##### Metody
- `__call__(self, text)`: (Brak docstringu)

#### `JSONParser`
(Brak docstringu)
##### Metody
- `__init__(self, spec, strict)`: (Brak docstringu)
- `schema(self)`: (Brak docstringu)
- `errors_to_markdown(errors)`: (Brak docstringu)
- `__call__(self, text)`: (Brak docstringu)

#### `EnumParser`
(Brak docstringu)
##### Metody
- `__init__(self, spec, ignore_case)`: (Brak docstringu)
- `__call__(self, text)`: (Brak docstringu)

#### `StringParser`
(Brak docstringu)
##### Metody
- `__call__(self, text)`: (Brak docstringu)


---
<a name="core_llm_prompt"></a>
## `core.llm.prompt`
(Brak docstringu modułu)

### <a name="klasy-core_llm_prompt"></a>Klasy
#### `FormatTemplate`
(Brak docstringu)
##### Metody
- `__call__(self, template, **kwargs)`: (Brak docstringu)

#### `BaseJinjaTemplate`
(Brak docstringu)
##### Metody
- `__init__(self, loader)`: (Brak docstringu)

#### `JinjaStringTemplate`
(Brak docstringu)
##### Metody
- `__init__(self)`: (Brak docstringu)
- `__call__(self, template, **kwargs)`: (Brak docstringu)

#### `JinjaFileTemplate`
(Brak docstringu)
##### Metody
- `__init__(self, template_dirs)`: (Brak docstringu)
- `__call__(self, template, **kwargs)`: (Brak docstringu)


---
<a name="core_llm_request_log"></a>
## `core.llm.request_log`
(Brak docstringu modułu)

### <a name="klasy-core_llm_request_log"></a>Klasy
#### `LLMRequestStatus`
(Brak docstringu)

#### `LLMRequestLog`
(Brak docstringu)


---
<a name="core_proc_exec_log"></a>
## `core.proc.exec_log`
(Brak docstringu modułu)

### <a name="klasy-core_proc_exec_log"></a>Klasy
#### `ExecLog`
(Brak docstringu)


---
<a name="core_proc_process_manager"></a>
## `core.proc.process_manager`
(Brak docstringu modułu)

### <a name="klasy-core_proc_process_manager"></a>Klasy
#### `LocalProcess`
(Brak docstringu)
##### Metody
- `__hash__(self)`: (Brak docstringu)
- `start(cmd)`: (Brak docstringu)
- `wait(self, timeout)`: (Brak docstringu)
- `read_output(self, timeout)`: (Brak docstringu)
- `terminate(self, kill)`: (Brak docstringu)
- `is_running(self)`: (Brak docstringu)
- `pid(self)`: (Brak docstringu)

#### `ProcessManager`
(Brak docstringu)
##### Metody
- `__init__(self)`: (Brak docstringu)
- `stop_watcher(self)`:
        Stop the process watcher.

        This should only be done when the ProcessManager is no longer needed.

- `watcher(self)`:
        Watch over the processes and manage their output and lifecycle.

        This is a separate coroutine running independently of the caller
        coroutine.

- `start_process(self, cmd)`: (Brak docstringu)
- `run_command(self, cmd)`:
        Run command and wait for it to finish.

        Status code is an integer representing the process exit code, or
        None if the process timed out and was terminated.

        :param cmd: Command to run.
        :param cwd: Working directory.
        :param env: Environment variables.
        :param timeout: Timeout in seconds.
        :param show_output: Show output in the ui.
        :return: Tuple of (status code, stdout, stderr).

- `list_running_processes(self)`: (Brak docstringu)
- `terminate_process(self, process_id)`: (Brak docstringu)


---
<a name="core_state_state_manager"></a>
## `core.state.state_manager`
(Brak docstringu modułu)

### <a name="klasy-core_state_state_manager"></a>Klasy
#### `StateManager`

    Manages loading, updating and saving project states.

    All project state references reading the current state
    should use `StateManager.current` attribute. All changes
    to the state should be done through the `StateManager.next`
    attribute.

##### Metody
- `__init__(self, session_manager, ui)`: (Brak docstringu)
- `db_blocker(self)`: (Brak docstringu)
- `list_projects(self)`:
        List projects with branches

        :return: List of projects with all their branches.

- `create_project(self, name, folder_name)`:
        Create a new project and set it as the current one.

        :param name: Project name.
        :return: The Project object.

- `delete_project(self, project_id)`: (Brak docstringu)
- `load_project(self)`:
        Load project state from the database.

        If `branch_id` is provided, load the latest state of the branch.
        Otherwise, if `project_id` is provided, load the latest state of
        the `main` branch in the project.

        If `step_index' is provided, load the state at the given step
        of the branch instead of the last one.

        The returned ProjectState will have branch and branch.project
        relationships preloaded. All other relationships must be
        explicitly loaded using ProjectState.awaitable_attrs or
        AsyncSession.refresh.

        :param project_id: Project ID (keyword-only, optional).
        :param branch_id: Branch ID (keyword-only, optional).
        :param step_index: Step index within the branch (keyword-only, optional).
        :return: The ProjectState object if found, None otherwise.

- `commit_with_retry(self)`: (Brak docstringu)
- `commit(self)`:
        Commit the new project state to the database.

        This commits `next_state` to the database, making the changes
        permanent, then creates a new state for further changes.

        :return: The committed state.

- `rollback(self)`:
        Abandon (rollback) the next state changes.

- `log_llm_request(self, request_log, agent)`:
        Log the request to the next state.

        Note: contrary to most other methods, this stores the information
        to the CURRENT state, not the next one. As the requests/responses
        depend on the current state, it makes it easier to analyze the
        database by just looking at a single project state later.

        :param request_log: The request log to log.

- `log_user_input(self, question, response)`:
        Log the user input to the current state.

        Note: contrary to most other methods, this stores the information
        to the CURRENT state, not the next one. As the user interactions
        depend on the current state, it makes it easier to analyze the
        database by just looking at a single project state later.

        :param question: The question asked.
        :param response: The user response.

- `log_command_run(self, exec_log)`:
        Log the command run to the current state.

        Note: contrary to most other methods, this stores the information
        to the CURRENT state, not the next one. As the command execution
        depend on the current state, it makes it easier to analyze the
        database by just looking at a single project state later.

        :param exec_log: The command execution log.

- `log_event(self, type, **kwargs)`:
        Log an event like:


        * start of epic
        * start of task
        * start of iteration
        * end of task
        * end of epic
        * loop detected

- `log_task_completed(self)`: (Brak docstringu)
- `get_file_by_path(self, path)`:
        Get a file from the current project state, by the file path.

        :param path: The file path.
        :return: The file object, or None if not found.

- `save_file(self, path, content, metadata, from_template)`:
        Save a file to the project.

        Note that the file is saved to the file system immediately, but in
        database it may be rolled back if `next_state` is never committed.

        :param path: The file path.
        :param content: The file content.
        :param metadata: Optional metadata (eg. description) to save with the file.
        :param from_template: Whether the file is part of a template.

- `init_file_system(self, load_existing)`:
        Initialize file system interface for the new or loaded project.

        When creating a new project, `load_existing` should be False to ensure a
        new unique project folder is created. When loading an existing project,
        `load_existing` should be True to allow using already-existing folder
        with the project files. If the folder doesn't exist, it will be created.

        This also initializes the ignore mechanism, so that files are correctly
        ignored as configured.

        :param load_existing: Whether to load existing files from the file system.
        :return: The file system interface.

- `get_full_project_root(self)`:
        Get the full path to the project root folder.

        :return: The full path to the project root folder.

- `import_files(self)`:
        Scan the file system, import new/modified files, delete removed files.

        The files are saved to / removed from `next_state`, but not committed
        to database until the new state is committed.

        :return: Tuple with the list of imported files and the list of removed files.

- `restore_files(self)`:
        Restore files from the database to VFS.

        Warning: this could overwrite user's files on disk!

        :return: List of restored files.

- `get_modified_files(self)`:
        Return a list of new or modified files from the file system.

        :return: List of paths for new or modified files.

- `get_modified_files_with_content(self)`:
        Return a list of new or modified files from the file system,
        including their paths, old content, and new content.

        :return: List of dictionaries containing paths, old content,
                and new content for new or modified files.

- `workspace_is_empty(self)`:
        Returns whether the workspace has any files in them or is empty.

- `get_implemented_pages(self)`:
        Get the list of implemented pages.

        :return: List of implemented pages.

- `update_implemented_pages_and_apis(self)`: (Brak docstringu)
- `update_utility_functions(self, utility_function)`:
        Update the knowledge base with the utility function.

        :param utility_function: Utility function to update.

- `get_apis(self)`:
        Get the list of APIs.

        :return: List of APIs.

- `update_apis(self, files_with_implemented_apis)`:
        Update the list of APIs.


- `get_input_required(content, file_path)`:
        Get the list of lines containing INPUT_REQUIRED keyword.

        :param content: The file content to search.
        :param file_path: The file path.
        :return: Indices of lines with INPUT_REQUIRED keyword, starting from 1.



---
<a name="core_templates_base"></a>
## `core.templates.base`
(Brak docstringu modułu)

### <a name="klasy-core_templates_base"></a>Klasy
#### `NoOptions`

    Options class for templates that do not require any options.


#### `BaseProjectTemplate`

    Base project template, providing a common interface for all project templates.

##### Metody
- `__init__(self, options, state_manager, process_manager)`:
        Create a new project template.

        :param options: The options to use for the template.
        :param state_manager: The state manager instance to save files to.
        :param process_manager: ProcessManager instance to run the install commands.

- `filter(self, path)`:
        Filter a file path to be included in the rendered template.

        The method is called for every file in the template tree before rendering.
        If the method returns None or an empty string, the file will be skipped.
        Otherwise, the file will be rendered and stored under the file name
        matching the provided filename.

        By default (base template), this function returns the path as-is.

        :param path: The file path to include or exclude.
        :return: The path to use, or None if the file should be skipped.

- `apply(self)`:
        Apply a project template to a new project.

        :param template_name: The name of the template to apply.
        :param state_manager: The state manager instance to save files to.
        :param process_manager: The process manager instance to run install hooks with.
        :return: A summary of the applied template, or None if no template was applied.

- `install_hook(self)`:
        Command to run to complete the project scaffolding setup.

- `options_dict(self)`: Template options as a Python dictionary.


---
<a name="core_templates_example_project"></a>
## `core.templates.example_project`
(Brak docstringu modułu)


---
<a name="core_templates_javascript_react"></a>
## `core.templates.javascript_react`
(Brak docstringu modułu)

### <a name="klasy-core_templates_javascript_react"></a>Klasy
#### `JavascriptReactProjectTemplate`
(Brak docstringu)
##### Metody
- `install_hook(self)`: (Brak docstringu)


---
<a name="core_templates_node_express_mongoose"></a>
## `core.templates.node_express_mongoose`
(Brak docstringu modułu)

### <a name="klasy-core_templates_node_express_mongoose"></a>Klasy
#### `NodeExpressMongooseProjectTemplate`
(Brak docstringu)
##### Metody
- `install_hook(self)`: (Brak docstringu)


---
<a name="core_templates_react_express"></a>
## `core.templates.react_express`
(Brak docstringu modułu)

### <a name="klasy-core_templates_react_express"></a>Klasy
#### `DatabaseType`
(Brak docstringu)

#### `TemplateOptions`
(Brak docstringu)

#### `ReactExpressProjectTemplate`
(Brak docstringu)
##### Metody
- `install_hook(self)`: (Brak docstringu)
- `filter(self, path)`: (Brak docstringu)


---
<a name="core_templates_registry"></a>
## `core.templates.registry`
(Brak docstringu modułu)

### <a name="klasy-core_templates_registry"></a>Klasy
#### `ProjectTemplateEnum`
Choices of available project templates.


---
<a name="core_templates_render"></a>
## `core.templates.render`
(Brak docstringu modułu)

### <a name="klasy-core_templates_render"></a>Klasy
#### `Renderer`

    Render a Jinja template

    Sets up Jinja renderer and renders one or more templates
    using provided context.

    * `render_template` renders a single template
    * `render_tree` renders all templates starting from a predefined
      root folder (which must reside inside templates folder structure)

    Rendered template(s) are returned as strings. Nothing is written
    to disk.

    Usage:

    >>> import Renderer from render
    >>> r = Renderer('path/to/templates')
    >>> output_string = r.render_template('template.html', {'key': 'value'})
    >>> output_tree = r.render_tree('tree/root', {'key': 'value'})

##### Metody
- `__init__(self, template_dir)`: (Brak docstringu)
- `render_template(self, template, context)`:
        Render a single template to a string using provided context

        :param template: Name of the template file, relative to `template_dir`.
        :param context: Context to render the template with.
        :return: The resulting string.

- `render_tree(self, root, context, full_root_dir, filter)`:
        Render a tree folder structure of templates using provided context

        :param root: Root of the tree (relative to `template_dir`).
        :param context: Context to render the templates with.
        :param full_root_dir: Full path to the root of the tree.
        :param filter: If defined, will be called for each file to check if it
        needs to be processed and determine output file path.
        :return: A flat dictionary with path => content structure.

        Root must be inside the template_dir (and must be specified relative
        to it), but need not be at the root of the template-dir.

        If supplied, `filter` must be a callable taking a single string
        argument. It will be called for every file before processing it, with
        the file name (relative to root of the tree) as the argument. If filter
        returns a non-empty string, file will be rendered. If it returns None
        or an empty string, file will be skipped. If `filter` is not defined,
        all files are processed.

        In the returned structure, `file_name` is location of the file
        relative to the tree root (unless changed by `filter`) and
        `contents` is file contents rendered to a binary (utf8-encoded) string.

        Directories are implied by file paths, not represented by elements
        in the returned dictionary.


### <a name="funkcje-core_templates_render"></a>Funkcje
- `escape_string(str)`:
    Escape special characters in a string

    :param str: The string to escape
    :return: The escaped string



---
<a name="core_templates_vite_react"></a>
## `core.templates.vite_react`
(Brak docstringu modułu)

### <a name="klasy-core_templates_vite_react"></a>Klasy
#### `ViteReactProjectTemplate`
(Brak docstringu)
##### Metody
- `install_hook(self)`: (Brak docstringu)


---
<a name="core_ui_base"></a>
## `core.ui.base`
(Brak docstringu modułu)

### <a name="klasy-core_ui_base"></a>Klasy
#### `ProjectStage`
(Brak docstringu)

#### `UIClosedError`
The user interface has been closed (user stoped Pythagora).

#### `UISource`

    Source for UI messages.

    See also: `AgentSource`

    Attributes:
    * `display_name`: Human-readable name of the source.
    * `type_name`: Type name of the source (used in IPC)

##### Metody
- `__init__(self, display_name, type_name)`:
        Create a new UI source.

        :param display_name: Human-readable name of the source.
        :param type_name: Type name of the source (used in IPC)

- `__str__(self)`: (Brak docstringu)

#### `AgentSource`

    Agent UI source.

    Attributes:
    * `display_name`: Human-readable name of the agent (eg. "Product Owner").
    * `type_name`: Type of the agent (eg. "agent:product-owner").

##### Metody
- `__init__(self, display_name, agent_type)`:
        Create a new agent source.

        :param display_name: Human-readable name of the agent.
        :param agent_type: Type of the agent.


#### `UserInput`

    Represents user input.

    See also: `UIBase.ask_question()`

    Attributes:
    * `text`: User-provided text (if any).
    * `button`: Name (key) of the button the user selected (if any).
    * `cancelled`: Whether the user cancelled the input.


#### `UIBase`

    Base class for UI adapters.

##### Metody
- `start(self)`:
        Start the UI adapter.

        :return: Whether the UI was started successfully.

- `stop(self)`:
        Stop the UI adapter.

- `send_stream_chunk(self, chunk)`:
        Send a chunk of the stream to the UI.

        :param chunk: Chunk of the stream.
        :param source: Source of the stream (if any).

- `send_message(self, message)`:
        Send a complete message to the UI.

        :param message: Message content.
        :param source: Source of the message (if any).
        :param project_state_id: Current project state id.
        :param extra_info: Extra information to indicate special functionality in extension.

- `send_key_expired(self, message)`:
        Send the key expired message.

- `send_app_finished(self, app_id, app_name, folder_name)`:
        Send the app finished message.

        :param app_id: App ID.
        :param app_name: App name.
        :param folder_name: Folder name.

- `send_feature_finished(self, app_id, app_name, folder_name)`:
        Send the feature finished message.

        :param app_id: App ID.
        :param app_name: App name.
        :param folder_name: Folder name.

- `ask_question(self, question)`:
        Ask the user a question.

        If buttons are provided, the UI should use the item values
        as button labels, and item keys as the values to return.

        After the user answers, constructs a `UserInput` object
        with the selected button or text. If the user cancels
        the input, the `cancelled` attribute should be set to True.

        :param project_state_id: Current project state id.
        :param initial_text: Placeholder for answer in extension.
        :param hint: Hint for question.
        :param question: Question to ask.
        :param buttons: Buttons to display (if any).
        :param default: Default value (if user provides no input).
        :param buttons_only: Whether to only show buttons (disallow custom text).
        :param allow_empty: Whether to allow empty input.
        :param full_screen: Ask question in full screen (IPC).
        :param verbose: Whether to log the question and response.
        :param source: Source of the question (if any).
        :param extra_info: Extra information to indicate special functionality in extension.
        :param placeholder: Placeholder text for the input field.
        :return: User input.

- `send_project_stage(self, data)`:
        Send a project stage to the UI.

        :param data: Project stage data.

- `send_epics_and_tasks(self, epics, tasks)`:
        Send epics and tasks info to the UI.

        :param epics: List of all epics.
        :param tasks: List of all tasks.

- `send_task_progress(self, index, n_tasks, description, source, status, source_index, tasks)`:
        Send a task progress update to the UI.

        :param index: Index of the current task, starting from 1.
        :param n_tasks: Total number of tasks.
        :param description: Description of the task.
        :param source: Source of the task, one of: 'app', 'feature', 'debugger', 'troubleshooting', 'review'.
        :param status: Status of the task, can be 'in_progress' or 'done'.
        :param source_index: Index of the source.
        :param tasks: List of all tasks.

- `send_step_progress(self, index, n_steps, step, task_source)`:
        Send a step progress update to the UI.

        :param index: Index of the step within the current task, starting from 1.
        :param n_steps: Number of steps in the current task.
        :param step: Step data.
        :param task_source: Source of the task, one of: 'app', 'feature', 'debugger', 'troubleshooting', 'review'.

- `send_modified_files(self, modified_files)`:
        Send a list of modified files to the UI.

        :param modified_files: List of modified files.

- `send_data_about_logs(self, data_about_logs)`:
        Send the data about debugging logs.

        :param data_about_logs: Data about logs.

- `send_run_command(self, run_command)`:
        Send a run command to the UI.

        :param run_command: Run command.

- `send_app_link(self, app_link)`:
        Send a run command to the UI.

        :param app_link: App link.

- `open_editor(self, file, line)`:
        Open an editor at the specified file and line.

        :param file: File to open.
        :param line: Line to highlight.

- `send_project_root(self, path)`:
        Tell UI component about the project root path.

        :param path: Project root path.

- `start_important_stream(self, path)`:
        Tell the extension that next stream should be visible and rendered as markdown


- `start_breakdown_stream(self)`:
        Tell the extension that breakdown stream will start.

- `send_project_stats(self, stats)`:
        Send project statistics to the UI.

        The stats object should have the following keys:
        * `num_lines` - Total number of lines in the project
        * `num_files` - Number of files in the project
        * `num_tokens` - Number of tokens used for LLM requests in this session

        :param stats: Project statistics.

- `send_test_instructions(self, test_instructions, project_state_id)`:
        Send test instructions.

        :param test_instructions: Test instructions.
        :param project_state_id: Project state ID.

- `knowledge_base_update(self, knowledge_base)`:
        Send updated knowledge base to the UI.

        :param knowledge_base: Knowledge base.

- `send_file_status(self, file_path, file_status, source)`:
        Send file status.

        :param file_path: File path.
        :param file_status: File status.
        :param source: Source of the file status.

- `send_bug_hunter_status(self, status, num_cycles)`:
        Send bug hunter status.

        :param status: Bug hunter status.
        :param num_cycles: Number of Bug hunter cycles.

- `generate_diff(self, file_path, file_old, file_new, n_new_lines, n_del_lines, source)`:
        Generate a diff between two files.

        :param file_path File path.
        :param file_old: Old file content.
        :param file_new: New file content.
        :param n_new_lines: Number of new lines.
        :param n_del_lines: Number of deleted lines.
        :param source: Source of the diff.

- `stop_app(self)`:
        Stop the App.

- `close_diff(self)`:
        Close all diff views.

- `loading_finished(self)`:
        Notify the UI that loading has finished.

- `send_project_description(self, description)`:
        Send the project description to the UI.

        :param description: Project description.

- `send_features_list(self, features)`:
        Send the summaries of implemented features to the UI.

        Features are epics after the initial one (initial project).

        :param features: List of feature summaries.

- `import_project(self, project_dir)`:
        Ask the UI to import files from the project directory.

        The UI should provide a way for the user to select the directory with
        existing project, and recursively copy the files over.

        :param project_dir: Project directory.



---
<a name="core_ui_console"></a>
## `core.ui.console`
(Brak docstringu modułu)

### <a name="klasy-core_ui_console"></a>Klasy
#### `PlainConsoleUI`

    UI adapter for plain (no color) console output.

##### Metody
- `start(self)`: (Brak docstringu)
- `stop(self)`: (Brak docstringu)
- `send_stream_chunk(self, chunk)`: (Brak docstringu)
- `send_message(self, message)`: (Brak docstringu)
- `send_key_expired(self, message)`: (Brak docstringu)
- `send_app_finished(self, app_id, app_name, folder_name)`: (Brak docstringu)
- `send_feature_finished(self, app_id, app_name, folder_name)`: (Brak docstringu)
- `ask_question(self, question)`: (Brak docstringu)
- `send_project_stage(self, data)`: (Brak docstringu)
- `send_epics_and_tasks(self, epics, tasks)`: (Brak docstringu)
- `send_task_progress(self, index, n_tasks, description, source, status, source_index, tasks)`: (Brak docstringu)
- `send_step_progress(self, index, n_steps, step, task_source)`: (Brak docstringu)
- `send_modified_files(self, modified_files)`: (Brak docstringu)
- `send_data_about_logs(self, data_about_logs)`: (Brak docstringu)
- `send_run_command(self, run_command)`: (Brak docstringu)
- `send_app_link(self, app_link)`: (Brak docstringu)
- `open_editor(self, file, line)`: (Brak docstringu)
- `send_project_root(self, path)`: (Brak docstringu)
- `send_project_stats(self, stats)`: (Brak docstringu)
- `send_test_instructions(self, test_instructions, project_state_id)`: (Brak docstringu)
- `knowledge_base_update(self, knowledge_base)`: (Brak docstringu)
- `send_file_status(self, file_path, file_status, source)`: (Brak docstringu)
- `send_bug_hunter_status(self, status, num_cycles)`: (Brak docstringu)
- `generate_diff(self, file_path, file_old, file_new, n_new_lines, n_del_lines, source)`: (Brak docstringu)
- `stop_app(self)`: (Brak docstringu)
- `close_diff(self)`: (Brak docstringu)
- `loading_finished(self)`: (Brak docstringu)
- `send_project_description(self, description)`: (Brak docstringu)
- `send_features_list(self, features)`: (Brak docstringu)
- `import_project(self, project_dir)`: (Brak docstringu)
- `start_important_stream(self)`: (Brak docstringu)
- `start_breakdown_stream(self)`: (Brak docstringu)


---
<a name="core_ui_ipc_client"></a>
## `core.ui.ipc_client`
(Brak docstringu modułu)

### <a name="klasy-core_ui_ipc_client"></a>Klasy
#### `MessageType`
(Brak docstringu)

#### `Message`

    Message structure for IPC communication with the VSCode extension.

    Attributes:
    * `type`: Message type (always "response" for VSC server responses)
    * `category`: Message category (eg. "agent:product-owner"), optional
    * `content`: Message content (eg. "Hello, how are you?"), optional

##### Metody
- `to_bytes(self)`:
        Convert Message instance to wire format.

- `from_bytes(self, data)`:
        Parses raw byte payload into a message.

        This is done in two phases. First, the bytes are UTF-8
        decoded and converted to a dict. Then, the dictionary
        structure is parsed into a Message object.

        This lets us raise different errors based on whether the
        data is not valid JSON or the JSON structure is not valid
        for a Message object.

        :param data: Raw byte payload.
        :return: Message object.


#### `IPCClientUI`

    UI adapter for Pythagora VSCode extension IPC.

##### Metody
- `__init__(self, config)`:
        Initialize the IPC client with the given configuration.

- `start(self)`: (Brak docstringu)
- `stop(self)`: (Brak docstringu)
- `send_stream_chunk(self, chunk)`: (Brak docstringu)
- `send_message(self, message)`: (Brak docstringu)
- `send_key_expired(self, message)`: (Brak docstringu)
- `send_app_finished(self, app_id, app_name, folder_name)`: (Brak docstringu)
- `send_feature_finished(self, app_id, app_name, folder_name)`: (Brak docstringu)
- `ask_question(self, question)`: (Brak docstringu)
- `send_project_stage(self, data)`: (Brak docstringu)
- `send_epics_and_tasks(self, epics, tasks)`: (Brak docstringu)
- `send_task_progress(self, index, n_tasks, description, source, status, source_index, tasks)`: (Brak docstringu)
- `send_modified_files(self, modified_files)`: (Brak docstringu)
- `send_step_progress(self, index, n_steps, step, task_source)`: (Brak docstringu)
- `send_data_about_logs(self, data_about_logs)`: (Brak docstringu)
- `send_run_command(self, run_command)`: (Brak docstringu)
- `send_app_link(self, app_link)`: (Brak docstringu)
- `open_editor(self, file, line)`: (Brak docstringu)
- `send_project_root(self, path)`: (Brak docstringu)
- `start_important_stream(self)`: (Brak docstringu)
- `start_breakdown_stream(self)`: (Brak docstringu)
- `send_project_stats(self, stats)`: (Brak docstringu)
- `send_test_instructions(self, test_instructions, project_state_id)`: (Brak docstringu)
- `knowledge_base_update(self, knowledge_base)`: (Brak docstringu)
- `send_file_status(self, file_path, file_status, source)`: (Brak docstringu)
- `send_bug_hunter_status(self, status, num_cycles)`: (Brak docstringu)
- `generate_diff(self, file_path, file_old, file_new, n_new_lines, n_del_lines, source)`: (Brak docstringu)
- `stop_app(self)`: (Brak docstringu)
- `close_diff(self)`: (Brak docstringu)
- `loading_finished(self)`: (Brak docstringu)
- `send_project_description(self, description)`: (Brak docstringu)
- `send_features_list(self, features)`: (Brak docstringu)
- `import_project(self, project_dir)`: (Brak docstringu)


---
<a name="core_ui_ipc_web_broker"></a>
## `core.ui.ipc_web_broker`

IPC Web Broker - Minimalny broker dla gemini-cli

TCP Server dla GPT-Pilot (port 8125) + HTTP API dla gemini-cli (port 8126)


### <a name="klasy-core_ui_ipc_web_broker"></a>Klasy
#### `BrokerConfig`
(Brak docstringu)

#### `MessageType`
(Brak docstringu)

#### `PendingQuestion`
(Brak docstringu)

#### `BrokerStats`
(Brak docstringu)
##### Metody
- `uptime(self)`: (Brak docstringu)

#### `IPCWebBroker`
Minimalny broker dla gemini-cli
##### Metody
- `__init__(self, config)`: (Brak docstringu)
- `handle_gpt_pilot_client(self, reader, writer)`: (Brak docstringu)
- `start_tcp_server(self)`: (Brak docstringu)
- `start_web_server(self)`: (Brak docstringu)
- `start(self)`: (Brak docstringu)

### <a name="funkcje-core_ui_ipc_web_broker"></a>Funkcje
- `main()`: (Brak docstringu)


---
<a name="core_ui_run_broker"></a>
## `core.ui.run_broker`

Skrypt uruchamiający IPC Web Broker


### <a name="funkcje-core_ui_run_broker"></a>Funkcje
- `main()`: Uruchom oba serwery


---
<a name="core_ui_virtual"></a>
## `core.ui.virtual`
(Brak docstringu modułu)

### <a name="klasy-core_ui_virtual"></a>Klasy
#### `VirtualUI`

    Testing UI adapter.

##### Metody
- `__init__(self, inputs)`: (Brak docstringu)
- `start(self)`: (Brak docstringu)
- `stop(self)`: (Brak docstringu)
- `send_stream_chunk(self, chunk)`: (Brak docstringu)
- `send_message(self, message)`: (Brak docstringu)
- `send_key_expired(self, message)`: (Brak docstringu)
- `send_app_finished(self, app_id, app_name, folder_name)`: (Brak docstringu)
- `send_feature_finished(self, app_id, app_name, folder_name)`: (Brak docstringu)
- `ask_question(self, question)`: (Brak docstringu)
- `send_project_stage(self, data)`: (Brak docstringu)
- `send_epics_and_tasks(self, epics, tasks)`: (Brak docstringu)
- `send_task_progress(self, index, n_tasks, description, source, status, source_index, tasks)`: (Brak docstringu)
- `send_step_progress(self, index, n_steps, step, task_source)`: (Brak docstringu)
- `send_data_about_logs(self, data_about_logs)`: (Brak docstringu)
- `send_modified_files(self, modified_files)`: (Brak docstringu)
- `send_run_command(self, run_command)`: (Brak docstringu)
- `send_app_link(self, app_link)`: (Brak docstringu)
- `open_editor(self, file, line)`: (Brak docstringu)
- `send_project_root(self, path)`: (Brak docstringu)
- `start_important_stream(self)`: (Brak docstringu)
- `start_breakdown_stream(self)`: (Brak docstringu)
- `send_project_stats(self, stats)`: (Brak docstringu)
- `send_test_instructions(self, test_instructions, project_state_id)`: (Brak docstringu)
- `knowledge_base_update(self, knowledge_base)`: (Brak docstringu)
- `send_file_status(self, file_path, file_status, source)`: (Brak docstringu)
- `send_bug_hunter_status(self, status, num_cycles)`: (Brak docstringu)
- `generate_diff(self, file_path, file_old, file_new, n_new_lines, n_del_lines, source)`: (Brak docstringu)
- `stop_app(self)`: (Brak docstringu)
- `close_diff(self)`: (Brak docstringu)
- `loading_finished(self)`: (Brak docstringu)
- `send_project_description(self, description)`: (Brak docstringu)
- `send_features_list(self, features)`: (Brak docstringu)
- `import_project(self, project_dir)`: (Brak docstringu)


---
<a name="core_ui_websocket_ui"></a>
## `core.ui.websocket_ui`
(Brak docstringu modułu)

### <a name="klasy-core_ui_websocket_ui"></a>Klasy
#### `WebSocketUIConfig`
Konfiguracja dla WebSocket UI
##### Metody
- `__init__(self, port, host)`: (Brak docstringu)

#### `WebSocketMessage`
Struktura wiadomości WebSocket
##### Metody
- `__init__(self, type, content, **kwargs)`: (Brak docstringu)
- `to_dict(self)`: (Brak docstringu)

#### `WebSocketUI`

    UI adapter używający WebSocket do komunikacji z interfejsem webowym.

    Wystawia serwer WebSocket na którym nasłuchuje połączeń od klientów webowych.
    Wszystkie wiadomości i pytania są przekazywane przez WebSocket.

##### Metody
- `__init__(self, config)`: (Brak docstringu)
- `start(self)`: Uruchom serwer WebSocket
- `stop(self)`: Zatrzymaj serwer WebSocket
- `send_stream_chunk(self, chunk)`: Wyślij fragment tekstu (streaming)
- `send_message(self, message)`: Wyślij wiadomość
- `ask_question(self, question)`: Zadaj pytanie i czekaj na odpowiedź przez WebSocket
- `send_key_expired(self, message)`: (Brak docstringu)
- `send_app_finished(self, app_id, app_name, folder_name)`: (Brak docstringu)
- `send_feature_finished(self, app_id, app_name, folder_name)`: (Brak docstringu)
- `send_project_stage(self, data)`: (Brak docstringu)
- `send_epics_and_tasks(self, epics, tasks)`: (Brak docstringu)
- `send_task_progress(self, index, n_tasks, description, source, status, source_index, tasks)`: (Brak docstringu)
- `send_step_progress(self, index, n_steps, step, task_source)`: (Brak docstringu)
- `send_modified_files(self, modified_files)`: (Brak docstringu)
- `send_data_about_logs(self, data_about_logs)`: (Brak docstringu)
- `send_run_command(self, run_command)`: (Brak docstringu)
- `send_app_link(self, app_link)`: (Brak docstringu)
- `open_editor(self, file, line)`: (Brak docstringu)
- `send_project_root(self, path)`: (Brak docstringu)
- `start_important_stream(self)`: (Brak docstringu)
- `start_breakdown_stream(self)`: (Brak docstringu)
- `send_project_stats(self, stats)`: (Brak docstringu)
- `send_test_instructions(self, test_instructions, project_state_id)`: (Brak docstringu)
- `knowledge_base_update(self, knowledge_base)`: (Brak docstringu)
- `send_file_status(self, file_path, file_status, source)`: (Brak docstringu)
- `send_bug_hunter_status(self, status, num_cycles)`: (Brak docstringu)
- `generate_diff(self, file_path, file_old, file_new, n_new_lines, n_del_lines, source)`: (Brak docstringu)
- `stop_app(self)`: (Brak docstringu)
- `close_diff(self)`: (Brak docstringu)
- `loading_finished(self)`: (Brak docstringu)
- `send_project_description(self, description)`: (Brak docstringu)
- `send_features_list(self, features)`: (Brak docstringu)
- `import_project(self, project_dir)`: (Brak docstringu)


---
<a name="core_db_models_base"></a>
## `core.db.models.base`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_base"></a>Klasy
#### `Base`
Base class for all SQL database models.
##### Metody
- `__repr__(self)`: Return a string representation of the model.


---
<a name="core_db_models_branch"></a>
## `core.db.models.branch`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_branch"></a>Klasy
#### `Branch`
(Brak docstringu)
##### Metody
- `get_by_id(session, branch_id)`:
        Get a project by ID.

        :param session: The SQLAlchemy session.
        :param project_id: The branch ID (as str or UUID value).
        :return: The Branch object if found, None otherwise.

- `get_last_state(self)`:
        Get the last project state of the branch.

        :return: The last step of the branch, or None if there are no steps.

- `get_state_at_step(self, step_index)`:
        Get the project state at the given step index for the branch.

        :return: The indicated step within the branch, or None if there's no such step.



---
<a name="core_db_models_exec_log"></a>
## `core.db.models.exec_log`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_exec_log"></a>Klasy
#### `ExecLog`
(Brak docstringu)
##### Metody
- `from_exec_log(cls, project_state, exec_log)`:
        Store the user input in the database.

        Note this just creates the UserInput object. It is committed to the
        database only when the DB session itself is comitted.

        :param project_state: Project state to associate the request log with.
        :param question: Question the user was asked.
        :param user_input: User input.
        :return: Newly created User input in the database.



---
<a name="core_db_models_file"></a>
## `core.db.models.file`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_file"></a>Klasy
#### `File`
(Brak docstringu)
##### Metody
- `clone(self)`:
        Clone the file object, to be used in a new project state.

        The clone references the same file content object as the original.

        :return: The cloned file object.



---
<a name="core_db_models_file_content"></a>
## `core.db.models.file_content`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_file_content"></a>Klasy
#### `FileContent`
(Brak docstringu)
##### Metody
- `store(cls, session, hash, content)`:
        Store the file content in the database.

        If the content is already stored, returns the reference to the existing
        content object. Otherwise stores it to the database and returns the newly
        created content object.

        :param session: The database session.
        :param hash: The hash of the file content, used as an unique ID.
        :param content: The file content as unicode string.
        :return: The file content object.

- `delete_orphans(cls, session)`:
        Delete FileContent objects that are not referenced by any File object.

        :param session: The database session.



---
<a name="core_db_models_llm_request"></a>
## `core.db.models.llm_request`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_llm_request"></a>Klasy
#### `LLMRequest`
(Brak docstringu)
##### Metody
- `from_request_log(cls, project_state, agent, request_log)`:
        Store the request log in the database.

        Note this just creates the request log object. It is committed to the
        database only when the DB session itself is comitted.

        :param project_state: Project state to associate the request log with.
        :param agent: Agent that made the request (if the caller was an agent).
        :param request_log: Request log.
        :return: Newly created LLM request log in the database.



---
<a name="core_db_models_project"></a>
## `core.db.models.project`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_project"></a>Klasy
#### `Project`
(Brak docstringu)
##### Metody
- `get_by_id(session, project_id)`:
        Get a project by ID.

        :param session: The SQLAlchemy session.
        :param project_id: The project ID (as str or UUID value).
        :return: The Project object if found, None otherwise.

- `get_branch(self, name)`:
        Get a project branch by name.

        :param session: The SQLAlchemy session.
        :param branch_name: The name of the branch (default "main").
        :return: The Branch object if found, None otherwise.

- `get_all_projects(session)`:
        Get all projects.

        This assumes the projects have at least one branch and one state.

        :param session: The SQLAlchemy session.
        :return: List of Project objects.

- `get_folder_from_project_name(name)`:
        Get the folder name from the project name.

        :param name: Project name.
        :return: Folder name.

- `delete_by_id(session, project_id)`:
        Delete a project by ID.

        :param session: The SQLAlchemy session.
        :param project_id: The project ID
        :return: Number of rows deleted.



---
<a name="core_db_models_project_state"></a>
## `core.db.models.project_state`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_project_state"></a>Klasy
#### `TaskStatus`
Status of a task.

#### `IterationStatus`
Status of an iteration.

#### `ProjectState`
(Brak docstringu)
##### Metody
- `unfinished_steps(self)`:
        Get the list of unfinished steps.

        :return: List of unfinished steps.

- `current_step(self)`:
        Get the current step.

        Current step is always the first step that's not finished yet.

        :return: The current step, or None if there are no more unfinished steps.

- `unfinished_iterations(self)`:
        Get the list of unfinished iterations.

        :return: List of unfinished iterations.

- `current_iteration(self)`:
        Get the current iteration.

        Current iteration is always the first iteration that's not finished yet.

        :return: The current iteration, or None if there are no unfinished iterations.

- `unfinished_tasks(self)`:
        Get the list of unfinished tasks.

        :return: List of unfinished tasks.

- `current_task(self)`:
        Get the current task.

        Current task is always the first task that's not finished yet.

        :return: The current task, or None if there are no unfinished tasks.

- `unfinished_epics(self)`:
        Get the list of unfinished epics.

        :return: List of unfinished epics.

- `current_epic(self)`:
        Get the current epic.

        Current epic is always the first epic that's not finished yet.

        :return: The current epic, or None if there are no unfinished epics.

- `relevant_file_objects(self)`:
        Get the relevant files with their content.

        :return: List of tuples with file path and content.

- `create_initial_state(branch)`:
        Create the initial project state for a new branch.

        This does *not* commit the new state to the database.

        No checks are made to ensure that the branch does not
        already have a state.

        :param branch: The branch to create the state for.
        :return: The new ProjectState object.

- `create_next_state(self)`:
        Create the next project state for the branch.

        This does NOT insert the new state and the associated objects (spec,
        files, ...) to the database.

        :param session: The SQLAlchemy session.
        :return: The new ProjectState object.

- `complete_step(self, step_type)`: (Brak docstringu)
- `complete_task(self)`: (Brak docstringu)
- `complete_epic(self)`: (Brak docstringu)
- `complete_iteration(self)`: (Brak docstringu)
- `flag_iterations_as_modified(self)`:
        Flag the iterations field as having been modified

        Used by Agents that perform modifications within the mutable iterations field,
        to tell the database that it was modified and should get saved (as SQLalchemy
        can't detect changes in mutable fields by itself).

- `flag_tasks_as_modified(self)`:
        Flag the tasks field as having been modified

        Used by Agents that perform modifications within the mutable tasks field,
        to tell the database that it was modified and should get saved (as SQLalchemy
        can't detect changes in mutable fields by itself).

- `flag_epics_as_modified(self)`:
        Flag the epic field as having been modified

        Used by Agents that perform modifications within the mutable epics field,
        to tell the database that it was modified and should get saved (as SQLalchemy
        can't detect changes in mutable fields by itself).

- `flag_knowledge_base_as_modified(self)`:
        Flag the knowledge base field as having been modified

        Used by Agents that perform modifications within the mutable knowledge base field,
        to tell the database that it was modified and should get saved (as SQLalchemy
        can't detect changes in mutable fields by itself).

- `set_current_task_status(self, status)`:
        Set the status of the current task.

        :param status: The new status.

- `get_file_by_path(self, path)`:
        Get a file from the current project state, by the file path.

        :param path: The file path.
        :return: The file object, or None if not found.

- `get_file_content_by_path(self, path)`:
        Get a file from the current project state, by the file path.

        :param path: The file path.
        :return: The file object, or None if not found.

- `save_file(self, path, content, external)`:
        Save a file to the project state.

        This either creates a new file pointing at the given content,
        or updates the content of an existing file. This method
        doesn't actually commit the file to the database, just attaches
        it to the project state.

        If the file was created by Pythagora (not externally by user or template import),
        mark it as relevant for the current task.

        :param path: The file path.
        :param content: The file content.
        :param external: Whether the file was added externally (e.g. by a user).
        :return: The (unsaved) file object.

- `delete_after(self)`:
        Delete all states in the branch after this one.

- `get_last_iteration_steps(self)`:
        Get the steps of the last iteration.

        :return: A list of steps.

- `get_source_index(self, source)`:
        Get the index of the source which can be one of: 'app', 'feature', 'troubleshooting', 'review'. For example,
        for feature return value would be number of current feature.

        :param source: The source to search for.
        :return: The index of the source.

- `get_steps_of_type(self, step_type)`:
        Get list of unfinished steps with specific type.

        :return: List of steps, or empty list if there are no unfinished steps of that type.

- `has_frontend(self)`:
        Check if there is a frontend epic in the project state.

        :return: True if there is a frontend epic, False otherwise.

- `is_feature(self)`:
        Check if the current epic is a feature.

        :return: True if the current epic is a feature, False otherwise.



---
<a name="core_db_models_specification"></a>
## `core.db.models.specification`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_specification"></a>Klasy
#### `Complexity`
Estimate of the project or feature complexity.

#### `Specification`
(Brak docstringu)
##### Metody
- `clone(self)`:
        Clone the specification.

- `delete_orphans(cls, session)`:
        Delete Specification objects that are not referenced by any ProjectState object.

        :param session: The database session.



---
<a name="core_db_models_user_input"></a>
## `core.db.models.user_input`
(Brak docstringu modułu)

### <a name="klasy-core_db_models_user_input"></a>Klasy
#### `UserInput`
(Brak docstringu)
##### Metody
- `from_user_input(cls, project_state, question, user_input)`:
        Store the user input in the database.

        Note this just creates the UserInput object. It is committed to the
        database only when the DB session itself is comitted.

        :param project_state: Project state to associate the request log with.
        :param question: Question the user was asked.
        :param user_input: User input.
        :return: Newly created User input in the database.
