from .base import BaseProjectTemplate, NoOptions


class ViteReactProjectTemplate(BaseProjectTemplate):
    stack = "backend"
    name = "vite_react"
    path = "vite_react"
    description = "Vite + React + Tailwind CSS + TypeScript + Shadcn + Nodejs + Mongo"
    file_descriptions = {
        "client/components.json": "Configuration file for UI component library, defining schema, styling options, and resource paths.",
        "client/eslint.config.js": "ESLint configuration file for TypeScript and React, including plugins and custom rules.",
        "client/index.html": "Main HTML entry point with root div for React mounting and main.tsx script.",
        "client/package.json": "Client configuration with dependencies, scripts, and metadata.",
        "client/postcss.config.js": "PostCSS configuration with tailwindcss and autoprefixer plugins.",
        "client/src/api/api.ts": "API utility function for fetching data from the server.",
        "client/src/api/auth.ts": "API utility functions for user authentication. Exports function login, register and logout.",
        "client/src/App.css": "Main application styles including root layout and animations.",
        "client/src/App.tsx": "Main React component with layout structure and welcome message.",
        "client/src/components/Footer.tsx": "Footer component with privacy and terms links.",
        "client/src/components/Header.tsx": "Header component with navigation menu.",
        "client/src/components/Layout.tsx": "Layout component with header, main content, and footer.",
        "client/src/components/ProtectedRoute.tsx": "Protected route component for authenticated user access control.",
        "client/src/components/ui/accordion.tsx": "Shadcn Accordion component. Exports Accordion, AccordionItem, AccordionButton, and AccordionPanel.",
        "client/src/components/ui/alert-dialog.tsx": "Shadcn Alert Dialog component. Exports   AlertDialog, AlertDialogPortal, AlertDialogOverlay, AlertDialogTrigger, AlertDialogContent, AlertDialogHeader, AlertDialogFooter, AlertDialogTitle, AlertDialogDescription, AlertDialogAction, AlertDialogCancel.",
        "client/src/components/ui/alert.tsx": "Shadcn Alert component. Exports Alert, AlertTitle, AlertDescription.",
        "client/src/components/ui/aspect-ratio.tsx": "Shadcn Aspect Ratio component. Exports AspectRatio.",
        "client/src/components/ui/avatar.tsx": "Shadcn Avatar component. Exports Avatar, AvatarImage, AvatarFallback.",
        "client/src/components/ui/badge.tsx": "Shadcn Badge component. Exports Badge, badgeVariants.",
        "client/src/components/ui/breadcrumb.tsx": "Shadcn Breadcrumb component. Exports Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator, BreadcrumbEllipsis.",
        "client/src/components/ui/button.tsx": "Shadcn Button component. Exports Button, buttonVariants.",
        "client/src/components/ui/calendar.tsx": "Shadcn Calendar component. Exports Calendar.",
        "client/src/components/ui/card.tsx": "Shadcn Card component. Exports Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent.",
        "client/src/components/ui/carousel.tsx": "Shadcn Carousel component. Exports type CarouselApi, Carousel, CarouselContent, CarouselItem, CarouselPrevious, CarouselNext.",
        "client/src/components/ui/chart.tsx": "Shadcn Chart component. Exports ChartContainer, ChartTooltip, ChartTooltipContent, ChartLegend, ChartLegendContent, ChartStyle.",
        "client/src/components/ui/checkbox.tsx": "Shadcn Checkbox component. Exports Checkbox.",
        "client/src/components/ui/collapsible.tsx": "Shadcn Collapsible component. Exports Collapsible, CollapsibleTrigger, CollapsibleContent.",
        "client/src/components/ui/command.tsx": "Shadcn Command component. Exports Command, CommandDialog, CommandInput, CommandList, CommandEmpty, CommandGroup, CommandItem, CommandShortcut, CommandSeparator.",
        "client/src/components/ui/context-menu.tsx": "Shadcn Context Menu component. Exports ContextMenu, ContextMenuTrigger, ContextMenuContent, ContextMenuItem, ContextMenuCheckboxItem, ContextMenuRadioItem, ContextMenuLabel, ContextMenuSeparator, ContextMenuShortcut, ContextMenuGroup, ContextMenuPortal, ContextMenuSub, ContextMenuSubContent, ContextMenuSubTrigger, ContextMenuRadioGroup.",
        "client/src/components/ui/dialog.tsx": "Shadcn Dialog component. Exports Dialog, DialogPortal, DialogOverlay, DialogClose, DialogTrigger, DialogContent, DialogHeader, DialogFooter, DialogTitle, DialogDescription.",
        "client/src/components/ui/drawer.tsx": "Shadcn Drawer component. Exports Drawer, DrawerPortal, DrawerOverlay, DrawerClose, DrawerTrigger, DrawerContent, DrawerHeader, DrawerFooter, DrawerTitle, DrawerDescription.",
        "client/src/components/ui/dropdown-menu.tsx": "Shadcn Dropdown Menu component. Exports DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem, DropdownMenuCheckboxItem, DropdownMenuRadioItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuShortcut, DropdownMenuGroup, DropdownMenuPortal, DropdownMenuSub, DropdownMenuSubContent, DropdownMenuSubTrigger, DropdownMenuRadioGroup.",
        "client/src/components/ui/form.tsx": "Shadcn Form component. Exports useFormField, Form, FormField, FormLabel, FormItem, FormControl, FormDescription, FormMessage.",
        "client/src/components/ui/hover-card.tsx": "Shadcn Hover Card component. Exports HoverCard, HoverCardTrigger, HoverCardContent.",
        "client/src/components/ui/input-otp.tsx": "Shadcn Input OTP component. Exports InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator.",
        "client/src/components/ui/input.tsx": "Shadcn Input component. Exports Input.",
        "client/src/components/ui/label.tsx": "Shadcn Label component. Exports Label.",
        "client/src/components/ui/menubar.tsx": "Shadcn Menubar component. Exports Menubar, MenubarMenu, MenubarTrigger, MenubarContent, MenubarItem, MenubarSeparator, MenubarLabel, MenubarCheckboxItem, MenubarRadioGroup, MenubarRadioItem, MenubarPortal, MenubarSubContent, MenubarSubTrigger, MenubarGroup, MenubarSub, MenubarShortcut.",
        "client/src/components/ui/navigation-menu.tsx": "Shadcn Navigation Menu component. Exports navigationMenuTriggerStyle, NavigationMenu, NavigationMenuList, NavigationMenuItem, NavigationMenuContent, NavigationMenuTrigger, NavigationMenuLink, NavigationMenuIndicator, NavigationMenuViewport.",
        "client/src/components/ui/pagination.tsx": "Shadcn Pagination component. Exports Pagination, PaginationContent, PaginationEllipsis, PaginationItem, PaginationLink, PaginationNext, PaginationPrevious.",
        "client/src/components/ui/popover.tsx": "Shadcn Popover component. Exports Popover, PopoverTrigger, PopoverContent.",
        "client/src/components/ui/progress.tsx": "Shadcn Progress component. Exports Progress.",
        "client/src/components/ui/radio-group.tsx": "Shadcn Radio Group component. Exports RadioGroup, RadioGroupItem.",
        "client/src/components/ui/resizable.tsx": "Shadcn Resizable component. Exports ResizablePanelGroup, ResizablePanel, ResizableHandle.",
        "client/src/components/ui/scroll-area.tsx": "Shadcn Scroll Area component. Exports ScrollArea, ScrollBar.",
        "client/src/components/ui/select.tsx": "Shadcn Select component. Exports Select, SelectGroup, SelectValue, SelectTrigger, SelectContent, SelectLabel, SelectItem, SelectSeparator, SelectScrollUpButton, SelectScrollDownButton.",
        "client/src/components/ui/separator.tsx": "Shadcn Separator component. Exports Separator.",
        "client/src/components/ui/sheet.tsx": "Shadcn Sheet component. Exports Sheet, SheetPortal, SheetOverlay, SheetClose, SheetTrigger, SheetContent, SheetHeader, SheetFooter, SheetTitle, SheetDescription.",
        "client/src/components/ui/sidebar.tsx": "Shadcn Sidebar component. Exports Sidebar, SidebarContent, SidebarFooter, SidebarGroup, SidebarGroupAction, SidebarGroupContent, SidebarGroupLabel, SidebarHeader, SidebarInput, SidebarInset, SidebarMenu, SidebarMenuAction, SidebarMenuBadge, SidebarMenuButton, SidebarMenuItem, SidebarMenuSkeleton, SidebarMenuSub, SidebarMenuSubButton, SidebarMenuSubItem, SidebarProvider, SidebarRail, SidebarSeparator, SidebarTrigger, useSidebar.",
        "client/src/components/ui/skeleton.tsx": "Shadcn Skeleton component. Exports Skeleton.",
        "client/src/components/ui/slider.tsx": "Shadcn Slider component. Exports Slider.",
        "client/src/components/ui/sonner.tsx": "Shadcn Sonner component. Exports Toaster.",
        "client/src/components/ui/switch.tsx": "Shadcn Switch component. Exports Switch.",
        "client/src/components/ui/table.tsx": "Shadcn Table component. Exports Table, TableBody, TableCell, TableFooter, TableHeader, TableHead, TableRow, TableCaption.",
        "client/src/components/ui/tabs.tsx": "Shadcn Tabs component. Exports Tabs, TabsList, TabsTrigger, TabsContent.",
        "client/src/components/ui/textarea.tsx": "Shadcn Textarea component. Exports Textarea.",
        "client/src/components/ui/theme-provider.tsx": "Theme provider component for managing light and dark mode themes.",
        "client/src/components/ui/theme-toggle.tsx": "Theme toggle component for switching between light and dark modes. Exports ThemeToggle.",
        "client/src/components/ui/toast.tsx": "Shadcn Toast component. Exports type ToastProps, type ToastActionElement, ToastProvider, ToastViewport, Toast, ToastTitle, ToastDescription, ToastClose, ToastAction.",
        "client/src/components/ui/toaster.tsx": "Shadcn Toaster component. Exports Toaster.",
        "client/src/components/ui/toggle-group.tsx": "Shadcn Toggle Group component. Exports ToggleGroup, ToggleGroupItem.",
        "client/src/components/ui/toggle.tsx": "Shadcn Toggle component. Exports Toggle, toggleVariants.",
        "client/src/components/ui/tooltip.tsx": "Shadcn Tooltip component. Exports Tooltip, TooltipTrigger, TooltipContent, TooltipProvider.",
        "client/src/contexts/AuthContext.tsx": "Context provider for user authentication state management. Exports AuthProvider, useAuth.",
        "client/src/hooks/useMobile.tsx": "Custom hook for detecting mobile viewport.",
        "client/src/hooks/useToast.ts": "Custom hook for managing toast notifications.",
        "client/src/index.css": "Global styles with Tailwind CSS configuration and theme variables.",
        "client/src/lib/utils.ts": "Utility functions for class name management.",
        "client/src/pages/Login.tsx": "Login page component with form for user authentication.",
        "client/src/pages/Register.tsx": "Registration page component with form for user registration.",
        "client/src/main.tsx": "Application entry point with React root rendering.",
        "client/src/vite-env.d.ts": "TypeScript declarations for Vite environment.",
        "tailwind.config.js": "Tailwind CSS configuration with theme customizations.",
        "client/tsconfig.app.json": "TypeScript configuration for application code.",
        "client/tsconfig.json": "Main TypeScript configuration with project references.",
        "client/tsconfig.node.json": "TypeScript configuration for Node.js environment.",
        "client/vite.config.ts": "Vite build tool configuration with React plugin and aliases.",
        "client/tailwind.config.js": "Tailwind CSS configuration with theme customizations, including enabling dark mode, specifying the content files that Tailwind should scan for class names, and extending the default theme with custom values for border radius, colors, keyframes, and animations. The configuration also includes a plugin for animations, specifically 'tailwindcss-animate', which allows for additional animation utilities to be used in the project.",
        "server/.env": "This file is a configuration file in the form of a .env file. It contains environment variables used by the application, such as the port to listen on, the MongoDB database URL, and the session secret string.",
        "server/server.js": "This `server.js` file sets up an Express server with MongoDB database connection, session management using connect-mongo, templating engine EJS, static file serving, authentication routes, error handling, and request logging. [References: dotenv, mongoose, express, express-session, connect-mongo, ./routes/authRoutes]",
        "server/package.json": "Server configuration with dependencies, scripts, and metadata. [References: server.js]",
        "server/config/database.js": "This file contains the database configuration for connecting to MongoDB using Mongoose. It exports a function that connects to the specified MongoDB URI and sets up event listeners for connection and error events. [References: mongoose]",
        "server/controllers/authController.js": "This file contains controller functions for user authentication, including registration, login, and logout. It interacts with the User model to handle user data and uses bcrypt for password hashing and comparison. [References: ../models/User.js, bcrypt]",
        "server/routes/authRoutes.js": "This file defines routes for user authentication including registration, login, and logout. It interacts with a User model to handle user data and uses bcrypt for password hashing and comparison. [References: models/User.js]",
        "server/routes/index.js": "This file defines routes for the home page.",
        "server/routes/middleware/auth.js": "This file defines a middleware function called requireUser, which checks if a user is authenticated based on the Authentication token in the header. If authenticated, it allows the request to proceed to the next middleware or route handler; otherwise, it returns a 403 status response indicating the user is not authenticated.",
        "server/models/User.js": "This file defines a Mongoose model for a user with fields for username and password. It includes a pre-save hook to hash the user's password before saving it to the database using bcrypt. [References: mongoose, bcrypt]",
        "server/services/llmService.js": "The file `llm.js` implements functionality for interacting with two large language model (LLM) providers: OpenAI and Anthropic. It uses the `axios` library for HTTP requests and the `dotenv` library to manage environment variables for API keys. The file defines functions to send requests to both providers, handling retries in case of errors. The `sendLLMRequest` function serves as a unified interface to send messages to either provider based on the specified provider name. The file exports sendLLMRequest() function for use in other parts of the application.",
        "server/services/userService.js": "The file `user.js` implements functionality for interacting with the User model defined in `models/User.js`. It includes functions to create a new user, find a user by username, and validate a user's password. The file exports createUser(...), list(...), get(...), getByEmail(...), update(...), delete(...), authenticateWithPassword(...), and setPassword(...) functions for use in other parts of the application.",
        "server/utils/auth.js": "This file defines utility functions for working with user authentication, including generateAccessToken and generateRefreshToken for generating JWT tokens. [References: jsonwebtoken]",
        "server/utils/password.js": "This file defines utility functions for working with passwords, including hashing and comparing passwords using the `bcrypt` library. [References: bcrypt]",
        "package.json": "Project configuration with dependencies, scripts, and metadata.",
        ".gitignore": "Git configuration to exclude files and directories from version control.",
    }
    summary = "\n".join([])
    options_class = NoOptions
    options_description = ""
    relevant_files = [
        "server/server.js",
        "server/routes/index.js",
        "client/components.json",
        "client/index.html",
        "client/package.json",
        "client/src/api/api.ts",
        "client/src/app.css",
        "client/src/App.tsx",
        "client/src/components/Footer.tsx",
        "client/src/components/Header.tsx",
        "client/src/components/Layout.tsx",
        "client/src/contexts/AuthContext.tsx",
        "client/src/index.css",
        "client/src/lib/utils.ts",
        "client/src/main.tsx",
        "client/src/vite-env.d.ts",
        "client/tailwind.config.js",
        "client/tsconfig.app.json",
        "client/tsconfig.json",
        "client/tsconfig.node.json",
        "client/vite.config.ts",
        "package.json",
    ]

    async def install_hook(self):
        await self.process_manager.run_command("npm install", show_output=False)
