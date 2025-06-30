# **Developer Productivity Dashboard - Full Specification**

## **Overview**

This document outlines the technical specifications for a "Developer Productivity Dashboard," a web application designed to serve as a central hub for development activities. Inspired by the GitHub dashboard, this application provides a unified interface for managing repositories, tracking issues and pull requests, and overseeing project progress. The goal is to streamline the developer workflow by consolidating key information and actions into a single, intuitive view.

## **Kluczowe Wytyczne Implementacyjne**

To ensure a seamless and consistent user experience, the highest priority during the development and extension of this application is full adherence to the existing UI/UX paradigm, which is based on the **shadcn/ui** component library.

1.  **Strict Adherence to Shadcn/ui**: All new pages, components, and UI elements must be constructed exclusively using standard, non-customized components from the `shadcn/ui` library. The objective is for new features to be visually and functionally indistinguishable from existing ones.
2.  **No Custom Styling**: The creation of local CSS classes, inline styles, or any other method of overriding the default `shadcn/ui` component appearance is strictly prohibited. The entire layout and design must rely on the pre-defined components and design tokens provided by the library.
3.  **Sidebar Integration**: New pages specified below (e.g., Repositories, Issues, Pull Requests) must be integrated into the main sidebar component. This includes adding the appropriate navigation links with icons and labels, preserving the existing structure and collapsible functionality.
4.  **Complete UI Implementation**: This task covers the full front-end implementation of the new pages, from creating the views and integrating navigation to arranging components in the main content area as detailed in this specification.

## **Core Layout & Navigation**

### **Main Interface Structure**

* **Top Navigation Bar**: A fixed header containing the global search bar, links to major sections like "Pull Requests" and "Issues," a "+" dropdown for quick actions (e.g., New Repository), and the user profile menu.
* **Left Sidebar**: A collapsible navigation panel providing access to a user's top repositories and teams. It will feature a filter to toggle between "Recent" and "All" repositories.
* **Main Content Area**: The primary workspace that dynamically renders content based on the user's selection. The default view is an activity feed.
* **Breadcrumb Navigation**: Displays the user's current location within the application's hierarchy (e.g., `Username / Repository Name / Issues`).

### **Left Sidebar Navigation Menu**

The sidebar is focused on direct access to code and collaboration hubs:

* **Dashboard** (Home icon) - The main landing page featuring an activity feed.
* **Repositories** (Repo icon) - A comprehensive list of user-associated repositories.
* **Issues** (Circle-Dot icon) - A global dashboard for tracking assigned issues.
* **Pull Requests** (Git Pull Request icon) - A global dashboard for managing pull requests.
* **Projects** (Project icon) - Kanban-style boards for project and task management.
* **Teams** (Users icon) - A list of teams the user is a member of.

## **Detailed Feature Specifications**

### **1. Global Search Engine**

* **Location**: Top Navigation Bar
* **Functionality**:
    * Universal search across repositories, code, issues, pull requests, users, and projects.
    * Dropdown with real-time suggestions and recently visited pages.
    * Support for search prefixes (`repo:`, `user:`, `is:issue`) to refine queries.
    * Executes a full-page search, presenting results in a categorized layout.
* **User Interactions**:
    * Clicking the search bar or using a keyboard shortcut (e.g., `Ctrl+K`) activates it.
    * Typing shows instant results categorized by type.
    * Pressing `Enter` navigates to a full search results page.

### **2. Repositories View**

* **Interface**: A filterable list of repositories, similar to GitHub's repository page.
* **Main Features**:
    * **Repository List**: Displays repository name, description, primary language, and last updated time.
    * **Search/Filter Bar**: Allows users to filter the list by name, language, or type (public, private, fork).
    * **"New" Button**: A prominent button to initiate the "Create a new repository" workflow.
    * **Starred Repositories**: A separate tab or filter to view repositories the user has starred.
* **User Interactions**:
    * Clicking a repository name navigates to that repository's dedicated page.
    * Using the filter bar instantly narrows down the repository list.
    * Clicking the "Star" icon next to a repository adds it to the user's starred list.

### **3. Issues Dashboard**

* **Interface**: A centralized view for managing issues across all repositories.
* **Main Features**:
    * **Tabbed Navigation**: Tabs to filter issues: "Created by you," "Assigned to you," "Mentioning you."
    * **Powerful Filtering**: A filter bar to narrow issues by author, repository, labels, projects, and milestones.
    * **Issue Row Component**: Each list item displays the issue title, repository source (`org/repo#ID`), labels, assignee, and time since last update.
    * **Bulk Actions**: Checkboxes to select multiple issues for bulk actions like adding labels or closing.
* **User Interactions**:
    * Clicking an issue title opens its detailed view.
    * Using the filter bar dynamically updates the list of issues.
    * Hovering over an issue can show a quick preview pop-up.

### **4. Pull Requests Dashboard**

* **Interface**: A dedicated dashboard for tracking the status of pull requests.
* **Main Features**:
    * **Tabbed Filtering**: Key tabs for "Created by you," "Awaiting your review," and "Assigned."
    * **PR Status Indicators**: Clear visual cues for PR status: Open, Merged, Closed, Draft. Icons also indicate CI/CD check status (pending, success, failure).
    * **Reviewer Information**: Displays the avatars of requested reviewers and those who have already commented.
    * **Advanced Filtering**: Filter by repository, author, reviewer, status, and labels.
* **User Interactions**:
    * Clicking a PR navigates to its "Conversation" view.
    * Users can approve or request changes from quick-action buttons directly in the list view.
    * The "Awaiting your review" tab is the default and highlights pending tasks.

### **5. Projects (Kanban Boards)**

* **Interface**: A flexible project management tool with Kanban boards, lists, and timeline views.
* **Main Features**:
    * **View Toggles**: Switch between Board, List, and Timeline (Gantt-style) views.
    * **Customizable Columns**: Users can create, rename, and rearrange columns on the Kanban board (e.g., "Backlog," "In Progress," "Done").
    * **Issue/PR Cards**: Cards on the board represent issues or pull requests, showing key details like title, assignee, and labels.
    * **Automation**: Set up rules to automatically move items between columns based on events (e.g., move to "Done" when a PR is merged).
* **User Interactions**:
    * Drag and drop cards between columns to update status.
    * Click a card to open a detailed side panel for the issue or PR.
    * Use the "+" button on a column to create a new draft issue for that status.

## **Required Third-Party Technologies**

### **Code & Text Processing**

* **Code Syntax Highlighting**: A library like `highlight.js` or `Prism.js` for displaying code snippets in issues and PRs.
* **Markdown Editor/Parser**: A robust Markdown library like `marked` or `react-markdown` for rendering user-generated content with GitHub Flavored Markdown (GFM) support.

### **API & Data Management**

* **State Management**: A client-side state management library like `Zustand` or `Redux Toolkit` for managing application state, especially for fetched data and UI state.
* **Data Fetching**: A library like `TanStack Query (React Query)` for declarative data fetching, caching, and synchronization with the backend API.

### **UI/UX Enhancement**

* **Charting Library**: A lightweight charting solution like `Recharts` or `Chart.js` for visualizing contribution activity on user profiles.
* **Drag-and-Drop**: `dnd-kit` or a similar library to enable reordering of items on Kanban boards and other interactive elements.
* **Icons**: An icon library such as `lucide-react` which integrates seamlessly with `shadcn/ui`.
* **Date/Time Formatting**: `date-fns` or a similar library for consistently formatting timestamps (e.g., "updated 2 hours ago").
