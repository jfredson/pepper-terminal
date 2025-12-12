                                                                  Pepper-Terminal Web Portal: Detailed Project Plan

                                                                                 1. Project Overview

Build a secure, user-friendly web portal for pepper-terminal that enables persistent, project-based conversational AI with layered memory. The portal will support multi-device
access, advanced memory management, and privacy controls.

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                               2. Architecture Choices

 • Frontend: React with TypeScript
    • SPA for responsive UI
    • Tailwind CSS for styling
    • React Router for navigation
    • State management with React Context or Zustand
 • Backend: Node.js with Express
    • RESTful API for user, project, and memory management
    • Integration with OpenAI API for AI responses
    • Command processing (:summarize, :new, etc.) handled server-side
 • Database: PostgreSQL
    • Stores users, projects, conversation logs, summaries                                                                                                                           
    • Enables scalable, relational data management                                                                                                                                   
 • Authentication: NextAuth.js with JWT                                                                                                                                              
    • Secure user login and session management                                                                                                                                       
    • Supports OAuth providers and email/password                                                                                                                                    
 • Hosting:                                                                                                                                                                          
    • Frontend: Vercel for easy deployment and CDN distribution                                                                                                                      
    • Backend: Heroku or DigitalOcean App Platform for scalable API hosting                                                                                                          
    • Database: Managed PostgreSQL (Heroku Postgres or DigitalOcean Managed DB)                                                                                                      
 • Security:                                                                                                                                                                         
    • HTTPS enforced                                                                                                                                                                 
    • Data encryption at rest and in transit                                                                                                                                         
    • Role-based access control if multi-user collaboration is added                                                                                                                 

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                            3. Core Features & Milestones                                                                            

                                                                                                                                                    
  Milestone                              Description                                                                                Estimated Time  
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
  M1: Setup & Foundations                Initialize frontend and backend repos, configure database, implement user authentication   1 week          
  M2: Project & Chat Management          CRUD for projects and chats, UI for project selection and creation                         1 week          
  M3: Conversation Logging               Store and retrieve chat messages per project, display chat history                         1 week          
  M4: AI Integration                     Connect backend to OpenAI API, inject memory context into prompts                          1 week          
  M5: Memory Summarization               Implement :summarize command, generate and store long-term summaries                       1 week          
  M6: Command Handling                   Support additional commands (:new, :clear, :summary) with UI controls                      1 week          
  M7: Context Window Management          Implement rolling recall window, inject summaries and recent messages                      1 week          
  M8: Export/Import Tools                Allow users to export/import project data for backup/offline use                           1 week          
  M9: UI/UX Refinements                  Improve responsiveness, accessibility, and user experience                                 1 week          
  M10: Security & Privacy Enhancements   Harden security, add encryption, privacy settings                                          1 week          
  M11: Deployment & Documentation        Deploy to production, write user and developer docs                                        1 week          
                                                                                                                                                    

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                4. Technical Details                                                                                 

 • API Endpoints Examples:                                                                                                                                                           
    • POST /api/auth/login — user login                                                                                                                                              
    • GET /api/projects — list user projects                                                                                                                                         
    • POST /api/projects — create new project                                                                                                                                        
    • GET /api/projects/:id/chats — get chat history                                                                                                                                 
    • POST /api/projects/:id/chats — add chat message                                                                                                                                
    • POST /api/projects/:id/commands — process commands like :summarize                                                                                                             
    • GET /api/projects/:id/summary — fetch long-term summary                                                                                                                        
 • Data Models:                                                                                                                                                                      
    • User: id, email, hashed_password, created_at                                                                                                                                   
    • Project: id, user_id, name, created_at, updated_at                                                                                                                             
    • ChatMessage: id, project_id, sender (user/assistant), content, timestamp                                                                                                       
    • Summary: id, project_id, content, last_updated                                                                                                                                 
 • Context Injection:                                                                                                                                                                
   Backend composes AI prompts by combining:                                                                                                                                         
    • Long-term summary (from Summary table)                                                                                                                                         
    • Recent chat messages (rolling recall window)                                                                                                                                   
    • Current user input                                                                                                                                                             

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                5. Development Tools                                                                                 

 • Version control: Git + GitHub                                                                                                                                                     
 • CI/CD: GitHub Actions for automated testing and deployment                                                                                                                        
 • Testing: Jest and React Testing Library for frontend, Mocha/Chai or Jest for backend                                                                                              
 • Linting/Formatting: ESLint, Prettier                                                                                                                                              
 • Containerization: Docker for local development and deployment                                                                                                                     

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                    6. Next Steps                                                                                    

 • Confirm architecture and tech stack choices                                                                                                                                       
 • Set up repositories and initial project scaffolding                                                                                                                               
 • Begin milestone M1: authentication and foundational setup
