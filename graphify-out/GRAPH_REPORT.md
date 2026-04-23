# Graph Report - /Users/prass/development/projects/repowire  (2026-04-23)

## Corpus Check
- 133 files · ~146,913 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1864 nodes · 5455 edges · 56 communities detected
- Extraction: 50% EXTRACTED · 50% INFERRED · 0% AMBIGUOUS · INFERRED: 2737 edges (avg confidence: 0.58)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Daemon App Core|Daemon App Core]]
- [[_COMMUNITY_CLI Commands|CLI Commands]]
- [[_COMMUNITY_Claude Code Installer|Claude Code Installer]]
- [[_COMMUNITY_Error Types|Error Types]]
- [[_COMMUNITY_Config & Models|Config & Models]]
- [[_COMMUNITY_Hook Adapters|Hook Adapters]]
- [[_COMMUNITY_FastAPI App State|FastAPI App State]]
- [[_COMMUNITY_App Lifecycle|App Lifecycle]]
- [[_COMMUNITY_Auth & API Key|Auth & API Key]]
- [[_COMMUNITY_Service Installer|Service Installer]]
- [[_COMMUNITY_Attachments API|Attachments API]]
- [[_COMMUNITY_CLAUDE.md Documentation|CLAUDE.md Documentation]]
- [[_COMMUNITY_Peer Registry|Peer Registry]]
- [[_COMMUNITY_Message Protocol|Message Protocol]]
- [[_COMMUNITY_Architecture Overview|Architecture Overview]]
- [[_COMMUNITY_WebSocket Hook|WebSocket Hook]]
- [[_COMMUNITY_Message Enum Types|Message Enum Types]]
- [[_COMMUNITY_Transcript Parsing|Transcript Parsing]]
- [[_COMMUNITY_Codex Installer|Codex Installer]]
- [[_COMMUNITY_Relay & Datastar|Relay & Datastar]]
- [[_COMMUNITY_Dashboard SSE Events|Dashboard SSE Events]]
- [[_COMMUNITY_Hook Handler Tests|Hook Handler Tests]]
- [[_COMMUNITY_Dashboard UI Components|Dashboard UI Components]]
- [[_COMMUNITY_Package Init Files|Package Init Files]]
- [[_COMMUNITY_Compose Bar UI|Compose Bar UI]]
- [[_COMMUNITY_Channel Transport|Channel Transport]]
- [[_COMMUNITY_Design System Tokens|Design System Tokens]]
- [[_COMMUNITY_App Layout|App Layout]]
- [[_COMMUNITY_Peer Label Types|Peer Label Types]]
- [[_COMMUNITY_Peer Header UI|Peer Header UI]]
- [[_COMMUNITY_Spawn Dialog|Spawn Dialog]]
- [[_COMMUNITY_Activity Feed UI|Activity Feed UI]]
- [[_COMMUNITY_Hero Component|Hero Component]]
- [[_COMMUNITY_Navbar Component|Navbar Component]]
- [[_COMMUNITY_Features Component|Features Component]]
- [[_COMMUNITY_Footer Component|Footer Component]]
- [[_COMMUNITY_Installation Component|Installation Component]]
- [[_COMMUNITY_Datastar Experiment|Datastar Experiment]]
- [[_COMMUNITY_Session Handler Tests|Session Handler Tests]]
- [[_COMMUNITY_Session Handler Tests|Session Handler Tests]]
- [[_COMMUNITY_Session Handler Tests|Session Handler Tests]]
- [[_COMMUNITY_Stop Handler Tests|Stop Handler Tests]]
- [[_COMMUNITY_Stop Handler Tests|Stop Handler Tests]]
- [[_COMMUNITY_Models Rationale|Models Rationale]]
- [[_COMMUNITY_Models Rationale|Models Rationale]]
- [[_COMMUNITY_Models Rationale|Models Rationale]]
- [[_COMMUNITY_Models Rationale|Models Rationale]]
- [[_COMMUNITY_Models Rationale|Models Rationale]]
- [[_COMMUNITY_Messages Rationale|Messages Rationale]]
- [[_COMMUNITY_Messages Rationale|Messages Rationale]]
- [[_COMMUNITY_Messages Rationale|Messages Rationale]]
- [[_COMMUNITY_Messages Rationale|Messages Rationale]]
- [[_COMMUNITY_Messages Rationale|Messages Rationale]]
- [[_COMMUNITY_Beads Issue Tracker|Beads Issue Tracker]]
- [[_COMMUNITY_Geist Font|Geist Font]]
- [[_COMMUNITY_Responsive Layout|Responsive Layout]]

## God Nodes (most connected - your core abstractions)
1. `AgentType` - 325 edges
2. `Config` - 276 edges
3. `PeerRegistry` - 205 edges
4. `PeerStatus` - 185 edges
5. `Peer` - 175 edges
6. `SpawnConfig` - 161 edges
7. `MessageRouter` - 155 edges
8. `WebSocketTransport` - 147 edges
9. `QueryTracker` - 141 edges
10. `PeerRole` - 138 edges

## Surprising Connections (you probably didn't know these)
- `React v1 Dashboard (replaced Datastar)` --semantically_similar_to--> `Next.js Dashboard (web/)`  [INFERRED] [semantically similar]
  experiments/datastar-dashboard/README.md → web/README.md
- `Compose Bar (Datastar peer_detail)` --semantically_similar_to--> `Compose Bar Component (design system)`  [INFERRED] [semantically similar]
  experiments/datastar-dashboard/templates/partials/peer_detail.html → docs/design-system.md
- `Peer Status Indicator (emerald/amber/zinc)` --semantically_similar_to--> `Status Indicators (Online/Busy/Offline)`  [INFERRED] [semantically similar]
  experiments/datastar-dashboard/templates/partials/peer_detail.html → docs/design-system.md
- `Check if this is a local peer.` --uses--> `AgentType`  [INFERRED]
  /Users/prass/development/projects/repowire/repowire/protocol/peers.py → /Users/prass/development/projects/repowire/repowire/config/models.py
- `Check if this peer runs OpenCode.` --uses--> `AgentType`  [INFERRED]
  /Users/prass/development/projects/repowire/repowire/protocol/peers.py → /Users/prass/development/projects/repowire/repowire/config/models.py

## Hyperedges (group relationships)
- **Daemon as Universal Routing Hub (all transports connect via WebSocket)** — readme_daemon, readme_hooks_transport, readme_channel_transport, readme_websocket_transport [EXTRACTED 0.95]
- **All Agents Use Hooks + MCP Pattern** — readme_claude_code_agent, readme_codex_agent, readme_gemini_agent, readme_opencode_agent, claude_hooks_adapters, claude_mcp_server_py [EXTRACTED 0.92]
- **Dashboard Design System Components (peer cards, status, compose bar)** — design_system_peer_cards, design_system_status_indicators, design_system_compose_bar_component, design_system_kinetic_mesh [EXTRACTED 0.88]
- **Agents Connect via Transport Layer to Daemon** — repowire_arch_claude_code, repowire_arch_codex, repowire_arch_gemini_cli, repowire_arch_opencode, repowire_arch_hooks_mcp, repowire_arch_plugin_ws, repowire_arch_daemon [EXTRACTED 1.00]
- **Daemon Internal Subsystems** — repowire_arch_daemon, repowire_arch_registry, repowire_arch_router, repowire_arch_transport [EXTRACTED 1.00]
- **Relay Enables Optional Remote Access** — repowire_arch_relay, repowire_arch_remote_dashboard, repowire_arch_cross_machine_mesh, repowire_arch_daemon [EXTRACTED 1.00]
- **Multiple Active Peers in Hosted Dashboard Mesh** — repowire_hosted_2_peer_repowire, repowire_hosted_2_peer_a2a_registry, repowire_hosted_2_peer_clusterkit, repowire_hosted_2_peer_modalkit, repowire_hosted_2_peer_phlow, repowire_hosted_2_peer_fastharness, repowire_hosted_2_peer_bananagraph, repowire_hosted_2_peer_agentdance [EXTRACTED 1.00]
- **Inter-peer Query/Response Communication Flow** — repowire_hosted_3_peer_a5b074db, repowire_hosted_3_clusterkit_peer, repowire_hosted_3_query_response, repowire_hosted_3_notify_messages [EXTRACTED 1.00]

## Communities

### Community 0 - "Daemon App Core"
Cohesion: 0.03
Nodes (212): Find the web output directory for the dashboard.      Checks dev mode first (rel, Create app for testing with optional mock components.      Args:         config:, Remove stale PID, log, and lock files from cache directory., Create and configure the FastAPI application.      Args:         config: Optiona, LifecycleHandler, Handles lifecycle events by updating the PeerRegistry.  This module has no knowl, No-op. Window renames must not rewrite peer display_name.          Why: Renaming, Log client detach. No state change for now. (+204 more)

### Community 1 - "CLI Commands"
Cohesion: 0.03
Nodes (193): peer_new(), Register a peer for mesh communication., Unregister a peer from the mesh., Ask a peer a question (CLI testing utility)., Remove offline peers from the daemon., Prompt user to configure a bot integration. Handles existing config display., Manage Claude Code hooks (alias for 'claude')., Install Repowire hooks into Claude Code. (+185 more)

### Community 2 - "Claude Code Installer"
Cohesion: 0.03
Nodes (132): check_channel_installed(), check_hooks_installed(), _find_channel_server(), get_claude_version(), _has_bun(), install_channel(), install_hooks(), _load_claude_settings() (+124 more)

### Community 3 - "Error Types"
Cohesion: 0.03
Nodes (61): DaemonConnectionError, DaemonError, DaemonHTTPError, DaemonTimeoutError, PeerDisconnectedError, Custom error types for Repowire protocol., Base class for daemon-related errors., Raised when the Repowire daemon is not reachable. (+53 more)

### Community 4 - "Config & Models"
Cohesion: 0.04
Nodes (54): cleanup_deps(), Cleanup dependencies. Called by app lifespan., DaemonConfig, dashboard_url(), effective_name(), effective_peer_id(), get_config_dir(), get_config_path() (+46 more)

### Community 5 - "Hook Adapters"
Cohesion: 0.04
Nodes (77): hook_output(), HookPayload, normalize(), Normalize agent-specific hook payloads into a common format.  Each agent runtime, Normalized hook payload, agent-agnostic., Normalize an agent-specific hook payload into a common format., Print required hook output to stdout. Gemini needs explicit approval., main() (+69 more)

### Community 6 - "FastAPI App State"
Cohesion: 0.05
Nodes (74): BaseModel, AppState, get_app_state(), get_config(), get_lifecycle_handler(), get_peer_registry(), init_deps(), FastAPI dependencies for the Repowire daemon. (+66 more)

### Community 7 - "App Lifecycle"
Cohesion: 0.05
Nodes (36): _cleanup_stale_artifacts(), create_app(), create_test_app(), _find_web_output_dir(), FastAPI application factory for the Repowire daemon., _esc(), _kb(), main() (+28 more)

### Community 8 - "Auth & API Key"
Cohesion: 0.06
Nodes (42): APIKey, Token-based authentication for the relay server.  Tokens are server-issued rando, Verify API key for relay mode.      Returns the API key if valid, None if auth i, A relay API key (token)., Issue a new token for a user. If user already has one, return it., Update the user_id for an auto-registered token., Dependency that requires authentication when relay mode is enabled., Validate a token. Auto-registers unknown but well-formed tokens.      Tokens are (+34 more)

### Community 9 - "Service Installer"
Cohesion: 0.07
Nodes (52): service_install(), service_status(), _generate_launchd_plist(), _generate_systemd_unit(), _get_launchd_plist_path(), _get_linux_service_status(), _get_log_path(), _get_macos_service_status() (+44 more)

### Community 10 - "Attachments API"
Cohesion: 0.06
Nodes (33): _cleanup_expired(), _ensure_dir(), get_attachment(), Attachment upload/download endpoints., Remove attachments older than MAX_AGE_HOURS. Best-effort., Upload a file attachment. Returns {id, path, filename, size}., Download an attachment by ID., upload_attachment() (+25 more)

### Community 11 - "CLAUDE.md Documentation"
Cohesion: 0.04
Nodes (54): AfterAgent Hook Event (Gemini), daemon/routes/attachments.py, BeforeAgent Hook Event (Gemini), channel/server.ts (MCP stdio transport), daemon/routes/ (HTTP endpoints), _ensure_registered() (MCP lazy identity), hooks/adapters.py (Hook Adapter), installers/claude_code.py (+46 more)

### Community 12 - "Peer Registry"
Cohesion: 0.11
Nodes (22): get_peer(), register_peer(), _make_manager(), _make_peer(), manager(), TestActiveRepairConcurrency, TestActiveRepairLiveness, TestGetPeerByPane (+14 more)

### Community 13 - "Message Protocol"
Cohesion: 0.09
Nodes (13): Convert to dictionary for serialization., Check if this is a local peer., Check if this peer runs OpenCode., Check if this peer runs Codex., Check if this peer runs Gemini., _make_peer(), Tests for repowire/protocol/peers.py — Peer model helpers., TestBackendHelpers (+5 more)

### Community 14 - "Architecture Overview"
Cohesion: 0.06
Nodes (43): Chat Bots (Telegram, Slack, ...), Claude Code Agent, Codex Agent, Cross-Machine Mesh, Daemon :8377 (local-first routing hub), Dashboard (localhost:8377), Gemini CLI Agent, hooks + MCP Transport (+35 more)

### Community 15 - "WebSocket Hook"
Cohesion: 0.09
Nodes (23): RuntimeError, Tests for websocket_hook helper functions., Tests for _is_pane_safe., tmux exits 0 with empty stdout for non-existent panes — must return False., Pane running a bare shell should return False., Pane running an agent binary should return True., Agent may report version string as pane_current_command — should return True., Nonzero returncode from tmux means pane is gone. (+15 more)

### Community 16 - "Message Enum Types"
Cohesion: 0.14
Nodes (18): Enum, BroadcastMessage, create(), from_dict(), Message, MessageType, NotificationMessage, QueryMessage (+10 more)

### Community 17 - "Transcript Parsing"
Cohesion: 0.13
Nodes (11): Stop hook firing on a pure tool-use turn must not re-emit the previous text resp, TestExtractLastTurnPair, TestExtractToolCalls, extract_last_turn_pair(), extract_last_turn_tool_calls(), _extract_text_from_content(), Claude Code transcript parser., Create a one-line summary of tool input. (+3 more)

### Community 18 - "Codex Installer"
Cohesion: 0.16
Nodes (22): check_hooks_installed(), check_mcp_installed(), _enable_hooks_feature(), get_codex_version(), install_hooks(), install_mcp(), _is_repowire_hook(), _load_hooks() (+14 more)

### Community 19 - "Relay & Datastar"
Cohesion: 0.09
Nodes (23): daemon/relay_client.py (outbound WSS), relay/server.py (FastAPI relay), dashboard.html (Datastar base template), Compose Bar (Datastar peer_detail), overview.html (Datastar partial), peer_detail.html (Datastar partial), Peer Status Indicator (emerald/amber/zinc), sidebar.html (Datastar partial) (+15 more)

### Community 20 - "Dashboard SSE Events"
Cohesion: 0.18
Nodes (19): _enrich_peer(), _format_event(), generate_sse_updates(), _peer_label(), Datastar-powered dashboard routes for the relay server.  Serves the dashboard HT, Render peer detail partial., Render the full dashboard HTML page with optional pre-rendered content., Generator that yields Datastar SSE events for live dashboard updates.      Args: (+11 more)

### Community 21 - "Hook Handler Tests"
Cohesion: 0.26
Nodes (9): Tests for prompt and notification hook handlers., _run_with_input(), test_gemini_before_agent(), test_no_pane_id(), test_sets_busy(), test_sets_online_on_idle(), test_status_update_failure(), TestNotificationHandler (+1 more)

### Community 22 - "Dashboard UI Components"
Cohesion: 0.23
Nodes (10): RoleBadge(), backendIcon(), cn(), roleBadgeClass(), shortPath(), statusBorderColor(), statusDot(), statusTextColor() (+2 more)

### Community 23 - "Package Init Files"
Cohesion: 0.22
Nodes (1): Agent-type-specific installers.

### Community 24 - "Compose Bar UI"
Cohesion: 0.8
Nodes (3): onKeyDown(), submit(), uploadFile()

### Community 25 - "Channel Transport"
Cohesion: 0.6
Nodes (3): connectDaemon(), fetchPeerContext(), scheduleReconnect()

### Community 26 - "Design System Tokens"
Cohesion: 0.5
Nodes (4): Full Color Token Set (Tailwind @theme), No-Line Rule (tonal boundary design), Surface Hierarchy Tokens, Typography System (Space Grotesk / Inter / JetBrains Mono)

### Community 27 - "App Layout"
Cohesion: 0.67
Nodes (1): RootLayout()

### Community 28 - "Peer Label Types"
Cohesion: 0.67
Nodes (1): peerLabel()

### Community 29 - "Peer Header UI"
Cohesion: 0.67
Nodes (1): copyName()

### Community 30 - "Spawn Dialog"
Cohesion: 0.67
Nodes (1): handleSpawn()

### Community 31 - "Activity Feed UI"
Cohesion: 0.67
Nodes (1): toggleItem()

### Community 32 - "Hero Component"
Cohesion: 0.67
Nodes (1): Hero()

### Community 33 - "Navbar Component"
Cohesion: 0.67
Nodes (1): Navbar()

### Community 34 - "Features Component"
Cohesion: 0.67
Nodes (1): Features()

### Community 35 - "Footer Component"
Cohesion: 0.67
Nodes (1): Footer()

### Community 36 - "Installation Component"
Cohesion: 0.67
Nodes (1): copyToClipboard()

### Community 37 - "Datastar Experiment"
Cohesion: 1.0
Nodes (2): experiments/datastar-dashboard/dashboard.py, Jinja2 Templates (Datastar experiment)

### Community 49 - "Session Handler Tests"
Cohesion: 1.0
Nodes (1): Repeated SessionStart for the same logical session skips ws-hook takeover.

### Community 50 - "Session Handler Tests"
Cohesion: 1.0
Nodes (1): Different cwd in same pane kills old ws-hook and re-registers.

### Community 51 - "Session Handler Tests"
Cohesion: 1.0
Nodes (1): Same cwd with a different hook session_id is treated as a fresh takeover.

### Community 53 - "Stop Handler Tests"
Cohesion: 1.0
Nodes (1): Chat turn payloads should include pane_id for server-side peer_id resolution.

### Community 54 - "Stop Handler Tests"
Cohesion: 1.0
Nodes (1): Test Gemini's AfterAgent hook which provides final_response but no transcript_pa

### Community 56 - "Models Rationale"
Cohesion: 1.0
Nodes (1): Dashboard URL via the relay, or None if not configured.

### Community 57 - "Models Rationale"
Cohesion: 1.0
Nodes (1): Get the effective peer name (display_name or fallback to name).

### Community 58 - "Models Rationale"
Cohesion: 1.0
Nodes (1): Get the effective peer_id (or generate legacy placeholder).

### Community 59 - "Models Rationale"
Cohesion: 1.0
Nodes (1): Get the Repowire config directory.

### Community 60 - "Models Rationale"
Cohesion: 1.0
Nodes (1): Get the config file path.

### Community 64 - "Messages Rationale"
Cohesion: 1.0
Nodes (1): Create from dictionary.

### Community 65 - "Messages Rationale"
Cohesion: 1.0
Nodes (1): Create a query message.

### Community 66 - "Messages Rationale"
Cohesion: 1.0
Nodes (1): Create a response message.

### Community 67 - "Messages Rationale"
Cohesion: 1.0
Nodes (1): Create a notification message.

### Community 68 - "Messages Rationale"
Cohesion: 1.0
Nodes (1): Create a broadcast message.

### Community 95 - "Beads Issue Tracker"
Cohesion: 1.0
Nodes (1): Beads Issue Tracker (bd)

### Community 96 - "Geist Font"
Cohesion: 1.0
Nodes (1): Geist Font (Vercel)

### Community 97 - "Responsive Layout"
Cohesion: 1.0
Nodes (1): Responsive Layout (Mobile + Desktop)

## Knowledge Gaps
- **247 isolated node(s):** `Human-readable label: folder name > session ID.`, `Returns (parent, folder) for display.`, `Add display helpers to a peer dict.`, `Add display helpers to an event dict.`, `Render sidebar partial.` (+242 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Package Init Files`** (9 nodes): `Agent-type-specific installers.`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `App Layout`** (3 nodes): `RootLayout()`, `layout.tsx`, `layout.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Peer Label Types`** (3 nodes): `peerLabel()`, `types.ts`, `types.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Peer Header UI`** (3 nodes): `copyName()`, `PeerHeader.tsx`, `PeerHeader.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Spawn Dialog`** (3 nodes): `handleSpawn()`, `SpawnDialog.tsx`, `SpawnDialog.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Activity Feed UI`** (3 nodes): `toggleItem()`, `ActivityFeed.tsx`, `ActivityFeed.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Hero Component`** (3 nodes): `Hero()`, `Hero.tsx`, `Hero.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Navbar Component`** (3 nodes): `Navbar()`, `Navbar.tsx`, `Navbar.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Features Component`** (3 nodes): `Features()`, `Features.tsx`, `Features.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Footer Component`** (3 nodes): `Footer()`, `Footer.tsx`, `Footer.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Installation Component`** (3 nodes): `copyToClipboard()`, `Installation.tsx`, `Installation.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Datastar Experiment`** (2 nodes): `experiments/datastar-dashboard/dashboard.py`, `Jinja2 Templates (Datastar experiment)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Session Handler Tests`** (1 nodes): `Repeated SessionStart for the same logical session skips ws-hook takeover.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Session Handler Tests`** (1 nodes): `Different cwd in same pane kills old ws-hook and re-registers.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Session Handler Tests`** (1 nodes): `Same cwd with a different hook session_id is treated as a fresh takeover.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Stop Handler Tests`** (1 nodes): `Chat turn payloads should include pane_id for server-side peer_id resolution.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Stop Handler Tests`** (1 nodes): `Test Gemini's AfterAgent hook which provides final_response but no transcript_pa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Models Rationale`** (1 nodes): `Dashboard URL via the relay, or None if not configured.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Models Rationale`** (1 nodes): `Get the effective peer name (display_name or fallback to name).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Models Rationale`** (1 nodes): `Get the effective peer_id (or generate legacy placeholder).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Models Rationale`** (1 nodes): `Get the Repowire config directory.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Models Rationale`** (1 nodes): `Get the config file path.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Messages Rationale`** (1 nodes): `Create from dictionary.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Messages Rationale`** (1 nodes): `Create a query message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Messages Rationale`** (1 nodes): `Create a response message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Messages Rationale`** (1 nodes): `Create a notification message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Messages Rationale`** (1 nodes): `Create a broadcast message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Beads Issue Tracker`** (1 nodes): `Beads Issue Tracker (bd)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Geist Font`** (1 nodes): `Geist Font (Vercel)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Responsive Layout`** (1 nodes): `Responsive Layout (Mobile + Desktop)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AgentType` connect `CLI Commands` to `Daemon App Core`, `Config & Models`, `Hook Adapters`, `FastAPI App State`, `App Lifecycle`, `Attachments API`, `Peer Registry`, `Message Protocol`, `WebSocket Hook`, `Message Enum Types`?**
  _High betweenness centrality (0.256) - this node is a cross-community bridge._
- **Why does `Config` connect `Daemon App Core` to `CLI Commands`, `Claude Code Installer`, `Config & Models`, `FastAPI App State`, `App Lifecycle`, `Attachments API`, `Peer Registry`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Why does `PeerRegistry` connect `Daemon App Core` to `CLI Commands`, `Config & Models`, `FastAPI App State`, `App Lifecycle`, `Attachments API`, `Peer Registry`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 320 inferred relationships involving `AgentType` (e.g. with `TestSpawnConfig` and `TestSpawnResult`) actually correct?**
  _`AgentType` has 320 INFERRED edges - model-reasoned connections that need verification._
- **Are the 269 inferred relationships involving `Config` (e.g. with `TestAppFactory` and `TestSpawnConfig`) actually correct?**
  _`Config` has 269 INFERRED edges - model-reasoned connections that need verification._
- **Are the 155 inferred relationships involving `PeerRegistry` (e.g. with `TestAppFactory` and `TestSpawnConfig`) actually correct?**
  _`PeerRegistry` has 155 INFERRED edges - model-reasoned connections that need verification._
- **Are the 180 inferred relationships involving `PeerStatus` (e.g. with `TestPeerCircleField` and `TestPeerConfigCircle`) actually correct?**
  _`PeerStatus` has 180 INFERRED edges - model-reasoned connections that need verification._