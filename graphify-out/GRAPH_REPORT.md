# Graph Report - /Users/prass/development/projects/repowire  (2026-04-27)

## Corpus Check
- 0 files · ~99,999 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1912 nodes · 5473 edges · 71 communities detected
- Extraction: 50% EXTRACTED · 50% INFERRED · 0% AMBIGUOUS · INFERRED: 2729 edges (avg confidence: 0.58)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Daemon Routing Core|Daemon Routing Core]]
- [[_COMMUNITY_CLI & Setup Commands|CLI & Setup Commands]]
- [[_COMMUNITY_FastAPI App Factory|FastAPI App Factory]]
- [[_COMMUNITY_Channel Installer|Channel Installer]]
- [[_COMMUNITY_Telegram Bot|Telegram Bot]]
- [[_COMMUNITY_Attachments|Attachments]]
- [[_COMMUNITY_Daemon Errors|Daemon Errors]]
- [[_COMMUNITY_Config & Persistence|Config & Persistence]]
- [[_COMMUNITY_Hook Adapter Normalization|Hook Adapter Normalization]]
- [[_COMMUNITY_Relay Auth Tokens|Relay Auth Tokens]]
- [[_COMMUNITY_Peer Registry Lifecycle|Peer Registry Lifecycle]]
- [[_COMMUNITY_Architecture Overview|Architecture Overview]]
- [[_COMMUNITY_Agent Type Enum|Agent Type Enum]]
- [[_COMMUNITY_Hooks Transport Utilities|Hooks Transport Utilities]]
- [[_COMMUNITY_WebSocket Hook Tests|WebSocket Hook Tests]]
- [[_COMMUNITY_Message Router Transport|Message Router Transport]]
- [[_COMMUNITY_Message Types|Message Types]]
- [[_COMMUNITY_Codex Installer|Codex Installer]]
- [[_COMMUNITY_Datastar Dashboard Routes|Datastar Dashboard Routes]]
- [[_COMMUNITY_Dashboard Templates|Dashboard Templates]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 72|Community 72]]
- [[_COMMUNITY_Community 73|Community 73]]
- [[_COMMUNITY_Community 74|Community 74]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 102|Community 102]]
- [[_COMMUNITY_Community 103|Community 103]]
- [[_COMMUNITY_Community 104|Community 104]]
- [[_COMMUNITY_Community 105|Community 105]]
- [[_COMMUNITY_Community 106|Community 106]]
- [[_COMMUNITY_Community 107|Community 107]]
- [[_COMMUNITY_Community 108|Community 108]]
- [[_COMMUNITY_Community 109|Community 109]]
- [[_COMMUNITY_Community 110|Community 110]]
- [[_COMMUNITY_Community 111|Community 111]]
- [[_COMMUNITY_Community 112|Community 112]]

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
- `_get_client()` --references--> `Hooks Transport (default)`  [INFERRED]
  /Users/prass/development/projects/repowire/repowire/hooks/utils.py → CLAUDE.md
- `Next.js Dashboard (web/)` --semantically_similar_to--> `React v1 Dashboard (replaced Datastar)`  [INFERRED] [semantically similar]
  web/README.md → experiments/datastar-dashboard/README.md
- `Compose Bar (Datastar peer_detail)` --semantically_similar_to--> `Compose Bar Component (design system)`  [INFERRED] [semantically similar]
  experiments/datastar-dashboard/templates/partials/peer_detail.html → docs/design-system.md
- `Peer Status Indicator (emerald/amber/zinc)` --semantically_similar_to--> `Status Indicators (Online/Busy/Offline)`  [INFERRED] [semantically similar]
  experiments/datastar-dashboard/templates/partials/peer_detail.html → docs/design-system.md
- `TelegramPeer` --references--> `Daemon-as-Routing-Hub Architecture`  [EXTRACTED]
  /Users/prass/development/projects/repowire/repowire/telegram/bot.py → CLAUDE.md

## Hyperedges (group relationships)
- **Telegram Reply-Keyboard Pipeline** — bot_compute_visible_recents, bot_build_reply_keyboard, bot_parse_keyboard_tap, bot_current_reply_keyboard, bot_on_text [EXTRACTED 0.90]
- **Hook → Daemon HTTP Layer (pooled client)** — utils_get_client, utils_daemon_post, utils_daemon_get, utils_update_status, utils_log_daemon_error [EXTRACTED 0.90]
- **OpenCode Incoming Query Lifecycle** — opencode_handle_incoming_query, opencode_resolve_session_id, opencode_active_model_tracking, opencode_ws_reconnect [EXTRACTED 0.85]

## Communities

### Community 0 - "Daemon Routing Core"
Cohesion: 0.03
Nodes (181): BaseModel, get_peer_registry(), MessageRouter, broadcast_message(), BroadcastRequest, BroadcastResponse, ChatTurnRequest, deliver_response() (+173 more)

### Community 1 - "CLI & Setup Commands"
Cohesion: 0.03
Nodes (192): peer_new(), Register a peer for mesh communication., Unregister a peer from the mesh., Ask a peer a question (CLI testing utility)., Remove offline peers from the daemon., Prompt user to configure a bot integration. Handles existing config display., Manage Claude Code hooks (alias for 'claude')., Install Repowire hooks into Claude Code. (+184 more)

### Community 2 - "FastAPI App Factory"
Cohesion: 0.03
Nodes (114): _cleanup_stale_artifacts(), create_app(), create_test_app(), _find_web_output_dir(), FastAPI application factory for the Repowire daemon., Find the web output directory for the dashboard.      Checks dev mode first (rel, Create app for testing with optional mock components.      Args:         config:, Remove stale PID, log, and lock files from cache directory. (+106 more)

### Community 3 - "Channel Installer"
Cohesion: 0.03
Nodes (129): check_channel_installed(), check_hooks_installed(), _find_channel_server(), get_claude_version(), _has_bun(), install_channel(), install_hooks(), _load_claude_settings() (+121 more)

### Community 4 - "Telegram Bot"
Cohesion: 0.03
Nodes (85): Telegram Photo Attachment Upload Flow, build_reply_keyboard(), TelegramPeer._cmd_peers, compute_visible_recents(), TelegramPeer._current_reply_keyboard, _esc(), TelegramPeer._fetch_online_peers, _kb() (+77 more)

### Community 5 - "Attachments"
Cohesion: 0.03
Nodes (95): _cleanup_expired(), _ensure_dir(), get_attachment(), Attachment upload/download endpoints., Remove attachments older than MAX_AGE_HOURS. Best-effort., Upload a file attachment. Returns {id, path, filename, size}., Download an attachment by ID., upload_attachment() (+87 more)

### Community 6 - "Daemon Errors"
Cohesion: 0.04
Nodes (54): DaemonConnectionError, DaemonError, DaemonHTTPError, DaemonTimeoutError, PeerDisconnectedError, Custom error types for Repowire protocol., Base class for daemon-related errors., Raised when the Repowire daemon is not reachable. (+46 more)

### Community 7 - "Config & Persistence"
Cohesion: 0.05
Nodes (39): dashboard_url(), effective_name(), effective_peer_id(), get_config_dir(), get_config_path(), LoggingConfig, Configuration models for Repowire., Settings controlling which commands and paths agents are allowed to spawn into. (+31 more)

### Community 8 - "Hook Adapter Normalization"
Cohesion: 0.05
Nodes (36): hook_output(), HookPayload, normalize(), Normalize agent-specific hook payloads into a common format.  Each agent runtime, Normalized hook payload, agent-agnostic., Normalize an agent-specific hook payload into a common format., Print required hook output to stdout. Gemini needs explicit approval., main() (+28 more)

### Community 9 - "Relay Auth Tokens"
Cohesion: 0.06
Nodes (42): APIKey, Token-based authentication for the relay server.  Tokens are server-issued rando, Verify API key for relay mode.      Returns the API key if valid, None if auth i, A relay API key (token)., Issue a new token for a user. If user already has one, return it., Update the user_id for an auto-registered token., Dependency that requires authentication when relay mode is enabled., Validate a token. Auto-registers unknown but well-formed tokens.      Tokens are (+34 more)

### Community 10 - "Peer Registry Lifecycle"
Cohesion: 0.11
Nodes (23): get_peer(), register_peer(), _make_manager(), _make_peer(), manager(), Tests for lazy_repair, active_repair, get_peer_by_pane, and ping/pong liveness., TestActiveRepairConcurrency, TestActiveRepairLiveness (+15 more)

### Community 11 - "Architecture Overview"
Cohesion: 0.06
Nodes (43): Chat Bots (Telegram, Slack, ...), Claude Code Agent, Codex Agent, Cross-Machine Mesh, Daemon :8377 (local-first routing hub), Dashboard (localhost:8377), Gemini CLI Agent, hooks + MCP Transport (+35 more)

### Community 12 - "Agent Type Enum"
Cohesion: 0.1
Nodes (12): Convert to dictionary for serialization., Check if this is a local peer., Check if this peer runs OpenCode., Check if this peer runs Codex., Check if this peer runs Gemini., _make_peer(), Tests for repowire/protocol/peers.py — Peer model helpers., TestBackendHelpers (+4 more)

### Community 13 - "Hooks Transport Utilities"
Cohesion: 0.08
Nodes (39): Hook Adapter (cross-agent normalization), Hooks Transport (default), MCP Server Identity / lazy registration, clear_pane_runtime_state(), clear_pending_cids(), daemon_get(), daemon_post(), _get_client() (+31 more)

### Community 14 - "WebSocket Hook Tests"
Cohesion: 0.1
Nodes (24): Tests for websocket_hook helper functions., Tests for _is_pane_safe., tmux exits 0 with empty stdout for non-existent panes — must return False., Pane running a bare shell should return False., Pane running an agent binary should return True., Agent may report version string as pane_current_command — should return True., Nonzero returncode from tmux means pane is gone., FileNotFoundError (tmux not found) should return False. (+16 more)

### Community 15 - "Message Router Transport"
Cohesion: 0.11
Nodes (12): Message routing logic.  Routes messages via WebSocket transport., Send notification (fire-and-forget).          Args:             from_peer: Displ, Tests for MessageRouter — query, notification, and broadcast delivery., router(), TestBroadcast, TestSendNotification, tracker(), transport() (+4 more)

### Community 16 - "Message Types"
Cohesion: 0.17
Nodes (15): Enum, BroadcastMessage, create(), from_dict(), Message, MessageType, NotificationMessage, QueryMessage (+7 more)

### Community 17 - "Codex Installer"
Cohesion: 0.16
Nodes (22): check_hooks_installed(), check_mcp_installed(), _enable_hooks_feature(), get_codex_version(), install_hooks(), install_mcp(), _is_repowire_hook(), _load_hooks() (+14 more)

### Community 18 - "Datastar Dashboard Routes"
Cohesion: 0.18
Nodes (19): _enrich_peer(), _format_event(), generate_sse_updates(), _peer_label(), Datastar-powered dashboard routes for the relay server.  Serves the dashboard HT, Render peer detail partial., Render the full dashboard HTML page with optional pre-rendered content., Generator that yields Datastar SSE events for live dashboard updates.      Args: (+11 more)

### Community 19 - "Dashboard Templates"
Cohesion: 0.1
Nodes (21): dashboard.html (Datastar base template), Compose Bar (Datastar peer_detail), overview.html (Datastar partial), peer_detail.html (Datastar partial), Peer Status Indicator (emerald/amber/zinc), sidebar.html (Datastar partial), SSE Init (@get /v2/sse) in base template, Cloudflare + SSE Incompatibility (lesson) (+13 more)

### Community 20 - "Community 20"
Cohesion: 0.26
Nodes (9): Tests for prompt and notification hook handlers., _run_with_input(), test_gemini_before_agent(), test_no_pane_id(), test_sets_busy(), test_sets_online_on_idle(), test_status_update_failure(), TestNotificationHandler (+1 more)

### Community 21 - "Community 21"
Cohesion: 0.23
Nodes (10): RoleBadge(), backendIcon(), cn(), roleBadgeClass(), shortPath(), statusBorderColor(), statusDot(), statusTextColor() (+2 more)

### Community 22 - "Community 22"
Cohesion: 0.2
Nodes (13): Agent Types Matrix, Daemon-as-Routing-Hub Architecture, Lazy Repair Design Philosophy, check_plugin_installed(), _get_plugin_path(), install_plugin(), OpenCode Plugin TypeScript Source, OpenCode plugin installer. (+5 more)

### Community 23 - "Community 23"
Cohesion: 0.18
Nodes (11): Development Environment Setup, Hooks Run from Installed Package (gotcha), Ruff Linter (line length 100), Channel Transport (Experimental), Claude Code Agent, OpenAI Codex Agent, Google Gemini CLI Agent, Hooks Transport (Default) (+3 more)

### Community 24 - "Community 24"
Cohesion: 0.2
Nodes (10): Circles (Logical Subnets), Context Breakout Problem (design rationale), HTTP Daemon (FastAPI :8377), Mesh Network for AI Coding Agents, OpenCode Agent, Repowire Project, Slack Bot Peer, Telegram Bot Peer (+2 more)

### Community 25 - "Community 25"
Cohesion: 0.22
Nodes (1): Agent-type-specific installers.

### Community 26 - "Community 26"
Cohesion: 0.61
Nodes (6): ClientDetachedRequest, PaneDiedRequest, Lifecycle event endpoints — provider-agnostic (tmux, containers, etc.)., SessionClosedRequest, SessionRenamedRequest, WindowRenamedRequest

### Community 27 - "Community 27"
Cohesion: 0.43
Nodes (5): health_check(), HealthResponse, Health check endpoint., Health check response., Check daemon health status.

### Community 28 - "Community 28"
Cohesion: 0.8
Nodes (3): onKeyDown(), submit(), uploadFile()

### Community 29 - "Community 29"
Cohesion: 0.6
Nodes (3): connectDaemon(), fetchPeerContext(), scheduleReconnect()

### Community 30 - "Community 30"
Cohesion: 0.5
Nodes (4): Full Color Token Set (Tailwind @theme), No-Line Rule (tonal boundary design), Surface Hierarchy Tokens, Typography System (Space Grotesk / Inter / JetBrains Mono)

### Community 31 - "Community 31"
Cohesion: 0.5
Nodes (4): AGENTS.md (symlink to CLAUDE.md), CLAUDE.md (codebase guide), Memory Sanitization Rules, Versioning Rules Rationale

### Community 32 - "Community 32"
Cohesion: 0.67
Nodes (1): RootLayout()

### Community 33 - "Community 33"
Cohesion: 0.67
Nodes (1): peerLabel()

### Community 34 - "Community 34"
Cohesion: 0.67
Nodes (1): copyName()

### Community 35 - "Community 35"
Cohesion: 0.67
Nodes (1): handleSpawn()

### Community 36 - "Community 36"
Cohesion: 0.67
Nodes (1): toggleItem()

### Community 37 - "Community 37"
Cohesion: 0.67
Nodes (1): Hero()

### Community 38 - "Community 38"
Cohesion: 0.67
Nodes (1): Navbar()

### Community 39 - "Community 39"
Cohesion: 0.67
Nodes (1): Features()

### Community 40 - "Community 40"
Cohesion: 0.67
Nodes (1): Footer()

### Community 41 - "Community 41"
Cohesion: 0.67
Nodes (1): copyToClipboard()

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (2): ask_peer MCP Tool, Correlation ID (ask_peer timeout 300s)

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (2): experiments/datastar-dashboard/dashboard.py, Jinja2 Templates (Datastar experiment)

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (2): Beads Issue Tracker integration, Session Completion Workflow

### Community 56 - "Community 56"
Cohesion: 1.0
Nodes (1): Repeated SessionStart for the same logical session skips ws-hook takeover.

### Community 57 - "Community 57"
Cohesion: 1.0
Nodes (1): Different cwd in same pane kills old ws-hook and re-registers.

### Community 58 - "Community 58"
Cohesion: 1.0
Nodes (1): Same cwd with a different hook session_id is treated as a fresh takeover.

### Community 60 - "Community 60"
Cohesion: 1.0
Nodes (1): Chat turn payloads should include pane_id for server-side peer_id resolution.

### Community 61 - "Community 61"
Cohesion: 1.0
Nodes (1): Test Gemini's AfterAgent hook which provides final_response but no transcript_pa

### Community 63 - "Community 63"
Cohesion: 1.0
Nodes (1): Dashboard URL via the relay, or None if not configured.

### Community 64 - "Community 64"
Cohesion: 1.0
Nodes (1): Get the effective peer name (display_name or fallback to name).

### Community 65 - "Community 65"
Cohesion: 1.0
Nodes (1): Get the effective peer_id (or generate legacy placeholder).

### Community 66 - "Community 66"
Cohesion: 1.0
Nodes (1): Get the Repowire config directory.

### Community 67 - "Community 67"
Cohesion: 1.0
Nodes (1): Get the config file path.

### Community 71 - "Community 71"
Cohesion: 1.0
Nodes (1): Create from dictionary.

### Community 72 - "Community 72"
Cohesion: 1.0
Nodes (1): Create a query message.

### Community 73 - "Community 73"
Cohesion: 1.0
Nodes (1): Create a response message.

### Community 74 - "Community 74"
Cohesion: 1.0
Nodes (1): Create a notification message.

### Community 75 - "Community 75"
Cohesion: 1.0
Nodes (1): Create a broadcast message.

### Community 102 - "Community 102"
Cohesion: 1.0
Nodes (1): notify_peer MCP Tool

### Community 103 - "Community 103"
Cohesion: 1.0
Nodes (1): broadcast MCP Tool

### Community 104 - "Community 104"
Cohesion: 1.0
Nodes (1): list_peers MCP Tool

### Community 105 - "Community 105"
Cohesion: 1.0
Nodes (1): whoami MCP Tool

### Community 106 - "Community 106"
Cohesion: 1.0
Nodes (1): set_description MCP Tool

### Community 107 - "Community 107"
Cohesion: 1.0
Nodes (1): spawn_peer MCP Tool

### Community 108 - "Community 108"
Cohesion: 1.0
Nodes (1): kill_peer MCP Tool

### Community 109 - "Community 109"
Cohesion: 1.0
Nodes (1): Lazy Repair Philosophy (CONTRIBUTING reference)

### Community 110 - "Community 110"
Cohesion: 1.0
Nodes (1): Geist Font (Vercel)

### Community 111 - "Community 111"
Cohesion: 1.0
Nodes (1): Responsive Layout (Mobile + Desktop)

### Community 112 - "Community 112"
Cohesion: 1.0
Nodes (1): Channel Transport (experimental)

## Knowledge Gaps
- **270 isolated node(s):** `Human-readable label: folder name > session ID.`, `Returns (parent, folder) for display.`, `Add display helpers to a peer dict.`, `Add display helpers to an event dict.`, `Render sidebar partial.` (+265 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 25`** (9 nodes): `Agent-type-specific installers.`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (3 nodes): `RootLayout()`, `layout.tsx`, `layout.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (3 nodes): `peerLabel()`, `types.ts`, `types.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (3 nodes): `copyName()`, `PeerHeader.tsx`, `PeerHeader.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (3 nodes): `handleSpawn()`, `SpawnDialog.tsx`, `SpawnDialog.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (3 nodes): `toggleItem()`, `ActivityFeed.tsx`, `ActivityFeed.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (3 nodes): `Hero()`, `Hero.tsx`, `Hero.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (3 nodes): `Navbar()`, `Navbar.tsx`, `Navbar.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (3 nodes): `Features()`, `Features.tsx`, `Features.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (3 nodes): `Footer()`, `Footer.tsx`, `Footer.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (3 nodes): `copyToClipboard()`, `Installation.tsx`, `Installation.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (2 nodes): `ask_peer MCP Tool`, `Correlation ID (ask_peer timeout 300s)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (2 nodes): `experiments/datastar-dashboard/dashboard.py`, `Jinja2 Templates (Datastar experiment)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (2 nodes): `Beads Issue Tracker integration`, `Session Completion Workflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `Repeated SessionStart for the same logical session skips ws-hook takeover.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `Different cwd in same pane kills old ws-hook and re-registers.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `Same cwd with a different hook session_id is treated as a fresh takeover.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (1 nodes): `Chat turn payloads should include pane_id for server-side peer_id resolution.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `Test Gemini's AfterAgent hook which provides final_response but no transcript_pa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `Dashboard URL via the relay, or None if not configured.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (1 nodes): `Get the effective peer name (display_name or fallback to name).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 65`** (1 nodes): `Get the effective peer_id (or generate legacy placeholder).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (1 nodes): `Get the Repowire config directory.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (1 nodes): `Get the config file path.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (1 nodes): `Create from dictionary.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 72`** (1 nodes): `Create a query message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 73`** (1 nodes): `Create a response message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (1 nodes): `Create a notification message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 75`** (1 nodes): `Create a broadcast message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 102`** (1 nodes): `notify_peer MCP Tool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 103`** (1 nodes): `broadcast MCP Tool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (1 nodes): `list_peers MCP Tool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 105`** (1 nodes): `whoami MCP Tool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 106`** (1 nodes): `set_description MCP Tool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (1 nodes): `spawn_peer MCP Tool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (1 nodes): `kill_peer MCP Tool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (1 nodes): `Lazy Repair Philosophy (CONTRIBUTING reference)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 110`** (1 nodes): `Geist Font (Vercel)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 111`** (1 nodes): `Responsive Layout (Mobile + Desktop)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 112`** (1 nodes): `Channel Transport (experimental)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AgentType` connect `CLI & Setup Commands` to `Daemon Routing Core`, `FastAPI App Factory`, `Telegram Bot`, `Attachments`, `Daemon Errors`, `Config & Persistence`, `Peer Registry Lifecycle`, `Agent Type Enum`, `WebSocket Hook Tests`, `Message Types`?**
  _High betweenness centrality (0.230) - this node is a cross-community bridge._
- **Why does `Config` connect `CLI & Setup Commands` to `Daemon Routing Core`, `FastAPI App Factory`, `Channel Installer`, `Telegram Bot`, `Config & Persistence`, `Peer Registry Lifecycle`, `Message Router Transport`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Why does `PeerRegistry` connect `FastAPI App Factory` to `Daemon Routing Core`, `CLI & Setup Commands`, `Telegram Bot`, `Daemon Errors`, `Peer Registry Lifecycle`, `Message Router Transport`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Are the 320 inferred relationships involving `AgentType` (e.g. with `TestSpawnConfig` and `TestSpawnResult`) actually correct?**
  _`AgentType` has 320 INFERRED edges - model-reasoned connections that need verification._
- **Are the 269 inferred relationships involving `Config` (e.g. with `_make_app()` and `TestAppFactory`) actually correct?**
  _`Config` has 269 INFERRED edges - model-reasoned connections that need verification._
- **Are the 155 inferred relationships involving `PeerRegistry` (e.g. with `_make_app()` and `TestAppFactory`) actually correct?**
  _`PeerRegistry` has 155 INFERRED edges - model-reasoned connections that need verification._
- **Are the 180 inferred relationships involving `PeerStatus` (e.g. with `TestPeerCircleField` and `TestPeerConfigCircle`) actually correct?**
  _`PeerStatus` has 180 INFERRED edges - model-reasoned connections that need verification._