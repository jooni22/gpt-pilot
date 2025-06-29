venv[stankiem@stankiem-x9srlf gpt-pilot]$ tree -I "node_modules" -I "__pycache__" -I "venv"
.
├── config-docker.json
├── config.json
├── core
│   ├── agents
│   │   ├── architect.py
│   │   ├── base.py
│   │   ├── bug_hunter.py
│   │   ├── code_monkey.py
│   │   ├── convo.py
│   │   ├── developer.py
│   │   ├── error_handler.py
│   │   ├── executor.py
│   │   ├── external_docs.py
│   │   ├── frontend.py
│   │   ├── git.py
│   │   ├── human_input.py
│   │   ├── importer.py
│   │   ├── __init__.py
│   │   ├── legacy_handler.py
│   │   ├── mixins.py
│   │   ├── orchestrator.py
│   │   ├── problem_solver.py
│   │   ├── response.py
│   │   ├── spec_writer.py
│   │   ├── task_completer.py
│   │   ├── tech_lead.py
│   │   ├── tech_writer.py
│   │   └── troubleshooter.py
│   ├── cli
│   │   ├── helpers.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── config
│   │   ├── env_importer.py
│   │   ├── __init__.py
│   │   ├── magic_words.py
│   │   ├── user_settings.py
│   │   └── version.py
│   ├── db
│   │   ├── alembic.ini
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── env.py
│   │   │   ├── README
│   │   │   ├── script.py.mako
│   │   │   └── versions
│   │   │       ├── 08d71952ec2f_refactor_specification_template_to_.py
│   │   │       ├── 0a1bb637fa26_initial.py
│   │   │       ├── b760f66138c0_add_docs_column_to_project_states.py
│   │   │       ├── c8905d4ce784_add_original_description_and_template_.py
│   │   │       ├── f352dbe45751_make_relevant_files_nullable.py
│   │   │       ├── f708791b9270_adding_knowledge_base_field_to_.py
│   │   │       └── ff891d366761_add_example_project_to_spec.py
│   │   ├── models
│   │   │   ├── base.py
│   │   │   ├── branch.py
│   │   │   ├── exec_log.py
│   │   │   ├── file_content.py
│   │   │   ├── file.py
│   │   │   ├── __init__.py
│   │   │   ├── llm_request.py
│   │   │   ├── project.py
│   │   │   ├── project_state.py
│   │   │   ├── specification.py
│   │   │   └── user_input.py
│   │   ├── session.py
│   │   ├── setup.py
│   │   └── v0importer.py
│   ├── disk
│   │   ├── ignore.py
│   │   ├── __init__.py
│   │   └── vfs.py
│   ├── llm
│   │   ├── anthropic_client.py
│   │   ├── azure_client.py
│   │   ├── base.py
│   │   ├── convo.py
│   │   ├── groq_client.py
│   │   ├── __init__.py
│   │   ├── openai_client.py
│   │   ├── parser.py
│   │   ├── prompt.py
│   │   └── request_log.py
│   ├── log
│   │   └── __init__.py
│   ├── proc
│   │   ├── exec_log.py
│   │   ├── __init__.py
│   │   └── process_manager.py
│   ├── prompts
│   │   ├── architect
│   │   │   ├── configure_template.prompt
│   │   │   ├── select_templates.prompt
│   │   │   ├── system.prompt
│   │   │   └── technologies.prompt
│   │   ├── bug-hunter
│   │   │   ├── ask_a_question.prompt
│   │   │   ├── bug_found_or_add_logs.prompt
│   │   │   ├── data_about_logs.prompt
│   │   │   ├── get_bug_reproduction_instructions.prompt
│   │   │   ├── instructions_from_human_hint.prompt
│   │   │   ├── iteration.prompt
│   │   │   ├── log_data.prompt
│   │   │   ├── problem_explanation.prompt
│   │   │   ├── system.prompt
│   │   │   └── tell_me_more.prompt
│   │   ├── code-monkey
│   │   │   ├── breakdown.prompt
│   │   │   ├── describe_file.prompt
│   │   │   ├── implement_changes.prompt
│   │   │   ├── iteration.prompt
│   │   │   ├── review_changes.prompt
│   │   │   ├── review_feedback.prompt
│   │   │   └── system.prompt
│   │   ├── developer
│   │   │   ├── breakdown.prompt
│   │   │   ├── filter_files_loop.prompt
│   │   │   ├── filter_files.prompt
│   │   │   ├── iteration.prompt
│   │   │   ├── parse_task.prompt
│   │   │   └── system.prompt
│   │   ├── error-handler
│   │   │   └── debug.prompt
│   │   ├── executor
│   │   │   └── ran_command.prompt
│   │   ├── external-docs
│   │   │   ├── create_docs_queries.prompt
│   │   │   ├── select_docset.prompt
│   │   │   └── system.prompt
│   │   ├── frontend
│   │   │   ├── build_frontend.prompt
│   │   │   └── system.prompt
│   │   ├── importer
│   │   │   ├── analyze_project.prompt
│   │   │   └── get_entrypoints.prompt
│   │   ├── partials
│   │   │   ├── breakdown_code_instructions.prompt
│   │   │   ├── coding_rules.prompt
│   │   │   ├── doc_snippets.prompt
│   │   │   ├── execution_order.prompt
│   │   │   ├── features_list.prompt
│   │   │   ├── file_naming.prompt
│   │   │   ├── files_descriptions.prompt
│   │   │   ├── file_size_limit.prompt
│   │   │   ├── files_list.prompt
│   │   │   ├── files_list_relevant.prompt
│   │   │   ├── filter_files_actions.prompt
│   │   │   ├── human_intervention_explanation.prompt
│   │   │   ├── project_details.prompt
│   │   │   ├── project_tasks.prompt
│   │   │   ├── relative_paths.prompt
│   │   │   └── user_feedback.prompt
│   │   ├── problem-solver
│   │   │   ├── get_alternative_solutions.prompt
│   │   │   ├── iteration.prompt
│   │   │   └── system.prompt
│   │   ├── pythagora
│   │   │   └── commit.prompt
│   │   ├── spec-writer
│   │   │   ├── add_new_feature.prompt
│   │   │   ├── ask_questions.prompt
│   │   │   ├── prompt_complexity.prompt
│   │   │   ├── review_spec.prompt
│   │   │   └── system.prompt
│   │   ├── tech-lead
│   │   │   ├── epic_breakdown.prompt
│   │   │   ├── filter_files_loop.prompt
│   │   │   ├── filter_files.prompt
│   │   │   ├── plan.prompt
│   │   │   └── system.prompt
│   │   ├── tech-writer
│   │   │   ├── create_readme.prompt
│   │   │   └── system.prompt
│   │   └── troubleshooter
│   │       ├── breakdown.prompt
│   │       ├── bug_report.prompt
│   │       ├── define_user_review_goal.prompt
│   │       ├── filter_files_loop.prompt
│   │       ├── filter_files.prompt
│   │       ├── get_route_files.prompt
│   │       ├── get_run_command.prompt
│   │       ├── iteration.prompt
│   │       └── system.prompt
│   ├── state
│   │   ├── __init__.py
│   │   └── state_manager.py
│   ├── telemetry
│   │   └── __init__.py
│   ├── templates
│   │   ├── base.py
│   │   ├── example_project.py
│   │   ├── info
│   │   │   ├── javascript_react
│   │   │   │   └── summary.tpl
│   │   │   ├── node_express_mongoose
│   │   │   │   └── summary.tpl
│   │   │   ├── react_express
│   │   │   │   └── summary.tpl
│   │   │   └── vite_react
│   │   │       └── summary.tpl
│   │   ├── __init__.py
│   │   ├── javascript_react.py
│   │   ├── node_express_mongoose.py
│   │   ├── react_express.py
│   │   ├── registry.py
│   │   ├── render.py
│   │   ├── tree
│   │   │   ├── add_raw_tags.py
│   │   │   ├── javascript_react
│   │   │   │   ├── index.html
│   │   │   │   ├── package.json
│   │   │   │   ├── public
│   │   │   │   ├── src
│   │   │   │   │   ├── App.css
│   │   │   │   │   ├── App.jsx
│   │   │   │   │   ├── assets
│   │   │   │   │   ├── index.css
│   │   │   │   │   └── main.jsx
│   │   │   │   └── vite.config.js
│   │   │   ├── node_express_mongoose
│   │   │   │   ├── models
│   │   │   │   │   └── User.js
│   │   │   │   ├── package.json
│   │   │   │   ├── public
│   │   │   │   │   ├── css
│   │   │   │   │   │   └── style.css
│   │   │   │   │   └── js
│   │   │   │   │       └── main.js
│   │   │   │   ├── routes
│   │   │   │   │   ├── authRoutes.js
│   │   │   │   │   └── middleware
│   │   │   │   │       └── authMiddleware.js
│   │   │   │   ├── server.js
│   │   │   │   ├── services
│   │   │   │   │   └── llm.js
│   │   │   │   └── views
│   │   │   │       ├── index.ejs
│   │   │   │       ├── login.ejs
│   │   │   │       ├── partials
│   │   │   │       │   ├── _footer.ejs
│   │   │   │       │   ├── _head.ejs
│   │   │   │       │   └── _header.ejs
│   │   │   │       └── register.ejs
│   │   │   ├── react_express
│   │   │   │   ├── api
│   │   │   │   │   ├── app.js
│   │   │   │   │   ├── middlewares
│   │   │   │   │   │   ├── authMiddleware.js
│   │   │   │   │   │   └── errorMiddleware.js
│   │   │   │   │   ├── models
│   │   │   │   │   │   ├── init.js
│   │   │   │   │   │   └── user.js
│   │   │   │   │   ├── routes
│   │   │   │   │   │   ├── authRoutes.js
│   │   │   │   │   │   └── index.js
│   │   │   │   │   ├── services
│   │   │   │   │   │   └── userService.js
│   │   │   │   │   └── utils
│   │   │   │   │       ├── log.js
│   │   │   │   │       ├── mail.js
│   │   │   │   │       └── password.js
│   │   │   │   ├── components.json
│   │   │   │   ├── index.html
│   │   │   │   ├── jsconfig.json
│   │   │   │   ├── package.json
│   │   │   │   ├── postcss.config.js
│   │   │   │   ├── prisma
│   │   │   │   │   └── schema.prisma
│   │   │   │   ├── public
│   │   │   │   ├── README.md
│   │   │   │   ├── server.js
│   │   │   │   ├── tailwind.config.js
│   │   │   │   ├── tsconfig.json
│   │   │   │   ├── ui
│   │   │   │   │   ├── assets
│   │   │   │   │   ├── components
│   │   │   │   │   │   └── ui
│   │   │   │   │   │       ├── alert.jsx
│   │   │   │   │   │       ├── button.jsx
│   │   │   │   │   │       ├── card.jsx
│   │   │   │   │   │       ├── input.jsx
│   │   │   │   │   │       └── label.jsx
│   │   │   │   │   ├── index.css
│   │   │   │   │   ├── lib
│   │   │   │   │   │   └── utils.js
│   │   │   │   │   ├── main.jsx
│   │   │   │   │   └── pages
│   │   │   │   │       ├── Home.css
│   │   │   │   │       ├── Home.jsx
│   │   │   │   │       ├── Login.jsx
│   │   │   │   │       └── Register.jsx
│   │   │   │   └── vite.config.js
│   │   │   └── vite_react
│   │   │       ├── client
│   │   │       │   ├── components.json
│   │   │       │   ├── eslint.config.js
│   │   │       │   ├── index.html
│   │   │       │   ├── package.json
│   │   │       │   ├── postcss.config.js
│   │   │       │   ├── public
│   │   │       │   │   └── favicon.ico
│   │   │       │   ├── src
│   │   │       │   │   ├── api
│   │   │       │   │   │   ├── api.ts
│   │   │       │   │   │   └── auth.ts
│   │   │       │   │   ├── App.css
│   │   │       │   │   ├── App.tsx
│   │   │       │   │   ├── components
│   │   │       │   │   │   ├── Footer.tsx
│   │   │       │   │   │   ├── Header.tsx
│   │   │       │   │   │   ├── Layout.tsx
│   │   │       │   │   │   ├── ProtectedRoute.tsx
│   │   │       │   │   │   └── ui
│   │   │       │   │   │       ├── accordion.tsx
│   │   │       │   │   │       ├── alert-dialog.tsx
│   │   │       │   │   │       ├── alert.tsx
│   │   │       │   │   │       ├── aspect-ratio.tsx
│   │   │       │   │   │       ├── avatar.tsx
│   │   │       │   │   │       ├── badge.tsx
│   │   │       │   │   │       ├── breadcrumb.tsx
│   │   │       │   │   │       ├── button.tsx
│   │   │       │   │   │       ├── calendar.tsx
│   │   │       │   │   │       ├── card.tsx
│   │   │       │   │   │       ├── carousel.tsx
│   │   │       │   │   │       ├── chart.tsx
│   │   │       │   │   │       ├── checkbox.tsx
│   │   │       │   │   │       ├── collapsible.tsx
│   │   │       │   │   │       ├── command.tsx
│   │   │       │   │   │       ├── context-menu.tsx
│   │   │       │   │   │       ├── dialog.tsx
│   │   │       │   │   │       ├── drawer.tsx
│   │   │       │   │   │       ├── dropdown-menu.tsx
│   │   │       │   │   │       ├── form.tsx
│   │   │       │   │   │       ├── hover-card.tsx
│   │   │       │   │   │       ├── input-otp.tsx
│   │   │       │   │   │       ├── input.tsx
│   │   │       │   │   │       ├── label.tsx
│   │   │       │   │   │       ├── menubar.tsx
│   │   │       │   │   │       ├── navigation-menu.tsx
│   │   │       │   │   │       ├── pagination.tsx
│   │   │       │   │   │       ├── popover.tsx
│   │   │       │   │   │       ├── progress.tsx
│   │   │       │   │   │       ├── radio-group.tsx
│   │   │       │   │   │       ├── resizable.tsx
│   │   │       │   │   │       ├── scroll-area.tsx
│   │   │       │   │   │       ├── select.tsx
│   │   │       │   │   │       ├── separator.tsx
│   │   │       │   │   │       ├── sheet.tsx
│   │   │       │   │   │       ├── sidebar.tsx
│   │   │       │   │   │       ├── skeleton.tsx
│   │   │       │   │   │       ├── slider.tsx
│   │   │       │   │   │       ├── sonner.tsx
│   │   │       │   │   │       ├── switch.tsx
│   │   │       │   │   │       ├── table.tsx
│   │   │       │   │   │       ├── tabs.tsx
│   │   │       │   │   │       ├── textarea.tsx
│   │   │       │   │   │       ├── theme-provider.tsx
│   │   │       │   │   │       ├── theme-toggle.tsx
│   │   │       │   │   │       ├── toaster.tsx
│   │   │       │   │   │       ├── toast.tsx
│   │   │       │   │   │       ├── toggle-group.tsx
│   │   │       │   │   │       ├── toggle.tsx
│   │   │       │   │   │       └── tooltip.tsx
│   │   │       │   │   ├── contexts
│   │   │       │   │   │   └── AuthContext.tsx
│   │   │       │   │   ├── hooks
│   │   │       │   │   │   ├── useMobile.tsx
│   │   │       │   │   │   └── useToast.ts
│   │   │       │   │   ├── index.css
│   │   │       │   │   ├── lib
│   │   │       │   │   │   └── utils.ts
│   │   │       │   │   ├── main.tsx
│   │   │       │   │   ├── pages
│   │   │       │   │   │   ├── Login.tsx
│   │   │       │   │   │   └── Register.tsx
│   │   │       │   │   └── vite-env.d.ts
│   │   │       │   ├── tailwind.config.js
│   │   │       │   ├── tsconfig.app.json
│   │   │       │   ├── tsconfig.json
│   │   │       │   ├── tsconfig.node.json
│   │   │       │   └── vite.config.ts
│   │   │       ├── package.json
│   │   │       └── server
│   │   │           ├── config
│   │   │           │   └── database.js
│   │   │           ├── models
│   │   │           │   ├── init.js
│   │   │           │   └── User.js
│   │   │           ├── package.json
│   │   │           ├── routes
│   │   │           │   ├── authRoutes.js
│   │   │           │   ├── index.js
│   │   │           │   └── middleware
│   │   │           │       └── auth.js
│   │   │           ├── server.js
│   │   │           ├── services
│   │   │           │   ├── llmService.js
│   │   │           │   └── userService.js
│   │   │           └── utils
│   │   │               ├── auth.js
│   │   │               └── password.js
│   │   └── vite_react.py
│   └── ui
│       ├── base.py
│       ├── console.py
│       ├── ipc_client.py
│       └── virtual.py
├── data
│   └── database
│       └── pythagora.db
├── Dockerfile
├── docs
│   ├── 0_pierwszy_prompt_apka_7tg_animacja.txt
│   ├── env.txt
│   ├── Groq
│   │   ├── API Error Codes and Responses - GroqDocs.md
│   │   ├── API Reference - GroqDocs.md
│   │   ├── Groq Client Libraries - GroqDocs.md
│   │   ├── OpenAI Compatibility - GroqDocs.md
│   │   ├── Quickstart - GroqDocs.md
│   │   ├── Reasoning - GroqDocs.md
│   │   ├── Supported Models - GroqDocs.md
│   │   ├── Templates - GroqDocs.md
│   │   └── Text Generation - GroqDocs.md
│   ├── llm_prompts.md
│   ├── TELEMETRY.md
│   ├── v2_wiki
│   └── Wiki
│       ├── Changing-Pythagora's-installation-directory.md
│       ├── Command-Execution.md
│       ├── Contact-Us.md
│       ├── Developing-locally-verses-in-the-cloud-with-Pythagora.md
│       ├── Frequently-Asked-Questions.md
│       ├── Home.md
│       ├── How-to-get-started-with-Pythagora.md
│       ├── How-to-update-the-Pythagora-VS-Code-extension.md
│       ├── How-to-upgrade-from-Pythagora-beta-to-Pythagora-v1.md
│       ├── How-to-write-a-good-initial-project-description.md
│       ├── Initial-project-description-examples.md
│       ├── Migrating-Applications-After-Updating-Pythagora-VS-Code-Extension.md
│       ├── Pythagora-App-Lab.md
│       ├── Using-GPT-Pilot-with-Anthropic-models.md
│       ├── Using-GPT‐Pilot-with-Local-LLMs.md
│       ├── Using-GPT-Pilot-with-OpenAI.md
│       ├── Using-MongoDB-with-Pythagora.md
│       ├── Using-Pythagora-with-your-own-OpenAI-key.md
│       └── Using-the-Pythagora-VS-Code-extension-with-your-own-API-key.md
├── entrypoint.sh
├── example-config.json
├── input.txt
├── LICENSE
├── litellm_config.yaml
├── main.py
├── on-event-extension-install.sh
├── pyproject.toml
├── pythagora.log
├── pythagora-vs-code.vsix
├── README.md
├── requirements.txt
├── run_interactive.sh
├── tests
│   ├── agents
│   │   ├── __init__.py
│   │   ├── test_base.py
│   │   ├── test_convo.py
│   │   ├── test_external_docs.py
│   │   ├── test_orchestrator.py
│   │   └── test_tech_lead.py
│   ├── cli
│   │   ├── __init__.py
│   │   └── test_cli.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── testconfig.json
│   │   ├── test_config.py
│   │   ├── test_env_importer.py
│   │   └── test_version.py
│   ├── conftest.py
│   ├── db
│   │   ├── factories.py
│   │   ├── __init__.py
│   │   ├── test_branch.py
│   │   ├── test_db.py
│   │   ├── test_project.py
│   │   └── test_project_state.py
│   ├── disk
│   │   ├── __init__.py
│   │   ├── test_ignore.py
│   │   └── test_vfs.py
│   ├── __init__.py
│   ├── integration
│   │   ├── __init__.py
│   │   └── llm
│   │       ├── __init__.py
│   │       ├── test_anthropic.py
│   │       ├── test_groq.py
│   │       └── test_openai.py
│   ├── llm
│   │   ├── __init__.py
│   │   ├── prompts
│   │   │   └── test.txt
│   │   ├── test_convo.py
│   │   ├── test_openai.py
│   │   ├── test_parser.py
│   │   └── test_prompt.py
│   ├── log
│   │   ├── __init__.py
│   │   └── test_log.py
│   ├── proc
│   │   ├── __init__.py
│   │   └── test_process_manager.py
│   ├── state
│   │   ├── __init__.py
│   │   └── test_state_manager.py
│   ├── telemetry
│   │   └── test_telemetry.py
│   ├── templates
│   │   └── test_templates.py
│   └── ui
│       ├── __init__.py
│       ├── test_console.py
│       └── test_ipc_client.py
└── workspace
    └── lklczxczxczx
        ├── client
        │   ├── components.json
        │   ├── eslint.config.js
        │   ├── index.html
        │   ├── package.json
        │   ├── package-lock.json
        │   ├── postcss.config.js
        │   ├── public
        │   │   └── favicon.ico
        │   ├── src
        │   │   ├── api
        │   │   │   ├── api.ts
        │   │   │   └── tableData.ts
        │   │   ├── App.css
        │   │   ├── App.tsx
        │   │   ├── components
        │   │   │   ├── Footer.tsx
        │   │   │   ├── Header.tsx
        │   │   │   ├── Layout.tsx
        │   │   │   ├── ProtectedRoute.tsx
        │   │   │   └── ui
        │   │   │       ├── accordion.tsx
        │   │   │       ├── alert-dialog.tsx
        │   │   │       ├── alert.tsx
        │   │   │       ├── aspect-ratio.tsx
        │   │   │       ├── avatar.tsx
        │   │   │       ├── badge.tsx
        │   │   │       ├── breadcrumb.tsx
        │   │   │       ├── button.tsx
        │   │   │       ├── calendar.tsx
        │   │   │       ├── card.tsx
        │   │   │       ├── carousel.tsx
        │   │   │       ├── chart.tsx
        │   │   │       ├── checkbox.tsx
        │   │   │       ├── collapsible.tsx
        │   │   │       ├── command.tsx
        │   │   │       ├── context-menu.tsx
        │   │   │       ├── dialog.tsx
        │   │   │       ├── drawer.tsx
        │   │   │       ├── dropdown-menu.tsx
        │   │   │       ├── form.tsx
        │   │   │       ├── hover-card.tsx
        │   │   │       ├── input-otp.tsx
        │   │   │       ├── input.tsx
        │   │   │       ├── label.tsx
        │   │   │       ├── menubar.tsx
        │   │   │       ├── navigation-menu.tsx
        │   │   │       ├── pagination.tsx
        │   │   │       ├── popover.tsx
        │   │   │       ├── progress.tsx
        │   │   │       ├── radio-group.tsx
        │   │   │       ├── resizable.tsx
        │   │   │       ├── scroll-area.tsx
        │   │   │       ├── select.tsx
        │   │   │       ├── separator.tsx
        │   │   │       ├── sheet.tsx
        │   │   │       ├── sidebar.tsx
        │   │   │       ├── skeleton.tsx
        │   │   │       ├── slider.tsx
        │   │   │       ├── sonner.tsx
        │   │   │       ├── switch.tsx
        │   │   │       ├── table.tsx
        │   │   │       ├── tabs.tsx
        │   │   │       ├── textarea.tsx
        │   │   │       ├── theme-provider.tsx
        │   │   │       ├── theme-toggle.tsx
        │   │   │       ├── toaster.tsx
        │   │   │       ├── toast.tsx
        │   │   │       ├── toggle-group.tsx
        │   │   │       ├── toggle.tsx
        │   │   │       └── tooltip.tsx
        │   │   ├── contexts
        │   │   │   └── AuthContext.tsx
        │   │   ├── hooks
        │   │   │   ├── useMobile.tsx
        │   │   │   └── useToast.ts
        │   │   ├── index.css
        │   │   ├── lib
        │   │   │   └── utils.ts
        │   │   ├── main.tsx
        │   │   ├── pages
        │   │   │   └── Home.tsx
        │   │   └── vite-env.d.ts
        │   ├── tailwind.config.js
        │   ├── tsconfig.app.json
        │   ├── tsconfig.json
        │   ├── tsconfig.node.json
        │   └── vite.config.ts
        ├── package.json
        ├── package-lock.json
        ├── pnpm-lock.yaml
        └── server
            ├── config
            │   └── database.js
            ├── package.json
            ├── package-lock.json
            ├── routes
            │   ├── index.js
            │   └── tableRoutes.js
            ├── server.js
            └── services
                ├── llmService.js
                └── tableService.js

125 directories, 503 files