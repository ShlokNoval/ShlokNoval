import os
import random

def generate_svg(mode):
    if mode == "dark":
        bg_color = "#030712"
        panel_color = "#0F172A"
        border_color = "rgba(255,255,255,0.08)"
        text_color = "#F8FAFC"
        muted_color = "#94A3B8"
        accent_1 = "#7C3AED"
        accent_2 = "#22D3EE"
        accent_3 = "#10B981"
        ascii_color_1 = "#22D3EE"
        ascii_color_2 = "#7C3AED"
        bg_glow_1 = "rgba(34, 211, 238, 0.15)"
        bg_glow_2 = "rgba(124, 58, 237, 0.15)"
        bg_glow_3 = "rgba(16, 185, 129, 0.15)"
    else:
        bg_color = "#FFFFFF"
        panel_color = "#F8FAFC"
        border_color = "rgba(15,23,42,0.08)"
        text_color = "#0F172A"
        muted_color = "#475569"
        accent_1 = "#2563EB"
        accent_2 = "#06B6D4"
        accent_3 = "#10B981"
        ascii_color_1 = "#2563EB"
        ascii_color_2 = "#06B6D4"
        bg_glow_1 = "rgba(37, 99, 235, 0.1)"
        bg_glow_2 = "rgba(6, 182, 212, 0.1)"
        bg_glow_3 = "rgba(16, 185, 129, 0.1)"
        
    width = 1180
    height = 610

    # Skills
    skills = ["React", "Next.js", "Node.js", "TypeScript", "Tailwind", "Python", "Docker", "Postgres", "AWS", "Git", "Figma"]

    # ASCII portrait lines
    ascii_art = [
        "      .::::::::...      ",
        "    .::::::::::::::::.    ",
        "  .::::::::::::::::::::.  ",
        " .::::::::::::::::::::::. ",
        " :::::::::::::::::::::::: ",
        " :::::::::::::::::::::::: ",
        " :::::::::::::::::::::::: ",
        " `::::::::::::::::::::::' ",
        "  `::::::::::::::::::::'  ",
        "    `::::::::::::::::'    ",
        "      `'::::::::::'`      ",
        "          ......          ",
        "      .::::::::::::.      ",
        "    .::::::::::::::::.    ",
        "  .::::::::::::::::::::.  "
    ]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <defs>
        <!-- Gradients -->
        <linearGradient id="accent-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{accent_1}">
                <animate attributeName="stop-color" values="{accent_1};{accent_2};{accent_3};{accent_1}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="50%" stop-color="{accent_2}">
                <animate attributeName="stop-color" values="{accent_2};{accent_3};{accent_1};{accent_2}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{accent_3}">
                <animate attributeName="stop-color" values="{accent_3};{accent_1};{accent_2};{accent_3}" dur="8s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <linearGradient id="ascii-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{ascii_color_1}">
                <animate attributeName="stop-color" values="{ascii_color_1};{ascii_color_2};{ascii_color_1}" dur="5s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{ascii_color_2}">
                <animate attributeName="stop-color" values="{ascii_color_2};{ascii_color_1};{ascii_color_2}" dur="5s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <!-- Filters -->
        <filter id="glow">
            <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <filter id="soft-glow">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <filter id="blur-bg">
            <feGaussianBlur stdDeviation="30"/>
        </filter>
        
        <filter id="noise">
            <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/>
            <feColorMatrix type="matrix" values="1 0 0 0 0, 0 1 0 0 0, 0 0 1 0 0, 0 0 0 0.05 0" />
        </filter>

        <!-- Clip Paths -->
        <clipPath id="typing-clip">
            <rect x="0" y="-30" width="0" height="60">
                <animate attributeName="width" values="0;280;280;0;0;280;280;0;0;280;280;0;0;280;280;0;0" keyTimes="0;0.05;0.2;0.25;0.3;0.35;0.5;0.55;0.6;0.65;0.8;0.85;0.9;0.95;0.98;0.99;1" dur="20s" repeatCount="indefinite" />
            </rect>
        </clipPath>

        <clipPath id="reveal-clip">
            <rect x="0" y="0" width="0" height="1000">
                <animate attributeName="width" values="0;1000" dur="2s" fill="freeze" begin="0.5s"/>
            </rect>
        </clipPath>

    </defs>

    <!-- Background -->
    <rect width="{width}" height="{height}" fill="{bg_color}" rx="24"/>
    
    <!-- Floating radial gradients -->
    <circle cx="200" cy="150" r="200" fill="{bg_glow_1}" filter="url(#blur-bg)">
        <animateMotion path="M 0,0 a 80,80 0 1,0 160,0 a 80,80 0 1,0 -160,0" dur="15s" repeatCount="indefinite" />
    </circle>
    <circle cx="900" cy="450" r="250" fill="{bg_glow_2}" filter="url(#blur-bg)">
        <animateMotion path="M 0,0 a -90,90 0 1,0 180,0 a -90,90 0 1,0 -180,0" dur="20s" repeatCount="indefinite" />
    </circle>
    <circle cx="600" cy="100" r="220" fill="{bg_glow_3}" filter="url(#blur-bg)">
        <animateMotion path="M 0,0 a 70,70 0 1,1 140,0 a 70,70 0 1,1 -140,0" dur="18s" repeatCount="indefinite" />
    </circle>
    
    <!-- Noise overlay -->
    <!-- The noise texture sometimes renders oddly on GitHub, but using it with 0.05 opacity shouldn't break anything. -->
    <rect width="{width}" height="{height}" style="pointer-events:none;" filter="url(#noise)" opacity="0.3" rx="24" />

    <!-- Particles -->
"""
    # Fix random seed so the animation feels consistent
    random.seed(42)
    for _ in range(25):
        px = random.randint(50, width - 50)
        py = random.randint(50, height - 50)
        r = random.uniform(1.0, 2.5)
        dur = random.uniform(4, 9)
        svg += f'    <circle cx="{px}" cy="{py}" r="{r}" fill="{text_color}" opacity="0">\n'
        svg += f'        <animate attributeName="opacity" values="0;0.6;0" dur="{dur}s" repeatCount="indefinite" />\n'
        svg += f'        <animate attributeName="cy" values="{py};{py-40};{py}" dur="{dur*1.5}s" repeatCount="indefinite" />\n'
        svg += '    </circle>\n'

    svg += f"""
    <!-- Left Side: ASCII Portrait -->
    <g transform="translate(40, 30)">
        <!-- Glass Panel -->
        <rect width="420" height="550" fill="{panel_color}" rx="16" fill-opacity="0.7" stroke="{border_color}" stroke-width="1.5">
            <animate attributeName="stroke" values="{border_color};{bg_glow_1};{border_color}" dur="4s" repeatCount="indefinite" />
        </rect>
        
        <!-- Border Shimmer -->
        <rect width="420" height="550" fill="none" rx="16" stroke="url(#accent-gradient)" stroke-width="2" opacity="0" stroke-dasharray="20 400" stroke-dashoffset="0">
            <animate attributeName="opacity" values="0;1;0" dur="6s" repeatCount="indefinite" />
            <animate attributeName="stroke-dashoffset" values="0;-420" dur="6s" repeatCount="indefinite" />
        </rect>

        <!-- Inner content floating -->
        <g>
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-10; 0,0" dur="6s" repeatCount="indefinite" />
            
            <text font-family="monospace" font-size="16" font-weight="bold" fill="url(#ascii-gradient)" filter="url(#glow)" x="210" y="100" text-anchor="middle" clip-path="url(#reveal-clip)">
"""
    y_offset = 120
    for idx, line in enumerate(ascii_art):
        begin_time = idx * 0.1
        # &#160; for spaces
        safe_line = line.replace(" ", "&#160;")
        svg += f'                <tspan x="210" y="{y_offset}" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.1s" begin="{begin_time}s" fill="freeze" />{safe_line}</tspan>\n'
        y_offset += 20
        
    svg += f"""            </text>
            
            <!-- Moving scanline -->
            <rect x="20" y="10" width="380" height="3" fill="url(#ascii-gradient)" opacity="0" filter="url(#glow)">
                <animate attributeName="opacity" values="0;0.5;0" dur="8s" repeatCount="indefinite" />
                <animate attributeName="y" values="10;540;10" dur="8s" repeatCount="indefinite" />
            </rect>
            
        </g>
    </g>

    <!-- Right Side: Terminal Window -->
    <g transform="translate(490, 30)">
        <!-- Glass Panel -->
        <rect width="650" height="550" fill="{panel_color}" rx="16" fill-opacity="0.7" stroke="{border_color}" stroke-width="1.5" />
        
        <!-- Terminal Header -->
        <rect width="650" height="40" fill="{border_color}" rx="16" />
        <rect width="650" height="20" y="20" fill="{border_color}" />
        <circle cx="30" cy="20" r="6" fill="#EF4444" />
        <circle cx="50" cy="20" r="6" fill="#F59E0B" />
        <circle cx="70" cy="20" r="6" fill="#10B981" />
        <text x="325" y="25" fill="{muted_color}" font-family="monospace" font-size="12" text-anchor="middle">~ / developer / profile</text>

        <!-- Content -->
        <g transform="translate(40, 80)">
            <g clip-path="url(#reveal-clip)">
                <!-- Greeting -->
                <text x="0" y="30" fill="{text_color}" font-family="system-ui, -apple-system, sans-serif" font-size="36" font-weight="bold">
                    Hi 👋 I'm Developer
                </text>
                
                <!-- Animated Typing Text -->
                <g transform="translate(0, 75)">
                    <text x="0" y="0" fill="url(#accent-gradient)" font-family="monospace" font-size="24" font-weight="bold" clip-path="url(#typing-clip)">
                        &gt; Frontend Engineer
                    </text>
                    <text x="0" y="0" fill="url(#accent-gradient)" font-family="monospace" font-size="24" font-weight="bold" clip-path="url(#typing-clip)" opacity="0">
                        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.25;0.25;0.55;0.55;1" dur="20s" repeatCount="indefinite" />
                        &gt; Full Stack Developer
                    </text>
                    <text x="0" y="0" fill="url(#accent-gradient)" font-family="monospace" font-size="24" font-weight="bold" clip-path="url(#typing-clip)" opacity="0">
                        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.55;0.55;0.85;0.85;1" dur="20s" repeatCount="indefinite" />
                        &gt; AI Enthusiast
                    </text>
                    <text x="0" y="0" fill="url(#accent-gradient)" font-family="monospace" font-size="24" font-weight="bold" clip-path="url(#typing-clip)" opacity="0">
                        <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.85;0.85;1" dur="20s" repeatCount="indefinite" />
                        &gt; Open Source Contributor
                    </text>
                    <!-- Blinking Cursor -->
                    <rect x="0" y="-22" width="12" height="26" fill="url(#accent-gradient)">
                        <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
                        <animate attributeName="x" values="24;310;310;24;24;330;330;24;24;260;260;24;24;380;380;24;24" keyTimes="0;0.05;0.2;0.25;0.3;0.35;0.5;0.55;0.6;0.65;0.8;0.85;0.9;0.95;0.98;0.99;1" dur="20s" repeatCount="indefinite" />
                    </rect>
                </g>

                <!-- Personal Info -->
                <g transform="translate(0, 140)" font-family="monospace" font-size="16" fill="{muted_color}">
                    <text x="0" y="0" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="1s" fill="freeze" /><tspan fill="{accent_2}">const</tspan> location = <tspan fill="{text_color}">"Earth"</tspan>;</text>
                    <text x="0" y="28" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.2s" fill="freeze" /><tspan fill="{accent_2}">const</tspan> education = <tspan fill="{text_color}">"Computer Science"</tspan>;</text>
                    <text x="0" y="56" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.4s" fill="freeze" /><tspan fill="{accent_2}">const</tspan> focus = <tspan fill="{text_color}">"Building Scalable Apps"</tspan>;</text>
                    <text x="0" y="84" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.6s" fill="freeze" /><tspan fill="{accent_2}">const</tspan> email = <tspan fill="{text_color}">"hello@example.com"</tspan>;</text>
                </g>

                <!-- Skills Section -->
                <g transform="translate(0, 270)">
                    <text x="0" y="0" fill="{text_color}" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="600" opacity="0">
                        <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2s" fill="freeze" />
                        Skills
                    </text>
                    
                    <g transform="translate(0, 20)">
"""
    
    # Glowing pills for skills
    sx, sy = 0, 0
    delay = 2.2
    for skill in skills:
        pill_width = len(skill) * 9 + 30
        if sx + pill_width > 570:
            sx = 0
            sy += 45
            
        svg += f"""
                        <g transform="translate({sx}, {sy})" opacity="0">
                            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="{delay}s" fill="freeze" />
                            <animateTransform attributeName="transform" type="translate" values="{sx},{sy+10}; {sx},{sy}" dur="0.5s" begin="{delay}s" fill="freeze" />
                            <rect width="{pill_width}" height="32" rx="16" fill="{border_color}" stroke="url(#accent-gradient)" stroke-width="1" />
                            <text x="{pill_width/2}" y="21" fill="{text_color}" font-family="system-ui, -apple-system, sans-serif" font-size="14" text-anchor="middle">{skill}</text>
                            
                            <rect width="{pill_width}" height="32" rx="16" fill="url(#accent-gradient)" opacity="0" filter="url(#glow)">
                                <animate attributeName="opacity" values="0; 0.2; 0" dur="{random.uniform(4, 7)}s" begin="{delay}s" repeatCount="indefinite" />
                            </rect>
                        </g>
"""
        sx += pill_width + 12
        delay += 0.1

    svg += f"""
                    </g>
                </g>

                <!-- Social Icons -->
                <g transform="translate(0, 420)" opacity="0">
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="3.5s" fill="freeze" />
                    <!-- GitHub -->
                    <g transform="translate(0, 0)">
                        <circle cx="20" cy="20" r="20" fill="{border_color}" />
                        <path d="M20,10 C14.477,10 10,14.477 10,20 C10,24.418 12.865,28.166 16.839,29.493 C17.339,29.585 17.522,29.277 17.522,29.014 C17.522,28.782 17.513,27.98 17.508,26.759 C14.726,27.362 14.139,25.645 14.139,25.645 C13.684,24.492 13.028,24.185 13.028,24.185 C12.121,23.565 13.097,23.578 13.097,23.578 C14.101,23.648 14.629,24.61 14.629,24.61 C15.521,26.14 16.969,25.698 17.541,25.437 C17.632,24.787 17.893,24.346 18.181,24.095 C15.959,23.843 13.626,22.984 13.626,19.475 C13.626,18.475 13.984,17.654 14.571,17.009 C14.476,16.757 14.162,15.827 14.661,14.542 C14.661,14.542 15.431,14.296 17.498,15.695 C18.229,15.492 19.006,15.39 19.775,15.387 C20.543,15.39 21.319,15.492 22.052,15.695 C24.117,14.296 24.885,14.542 24.885,14.542 C25.385,15.827 25.072,16.757 24.978,17.009 C25.567,17.654 25.922,18.475 25.922,19.475 C25.922,22.993 23.585,23.84 21.356,24.085 C21.719,24.398 22.045,25.016 22.045,25.962 C22.045,27.317 22.033,28.406 22.033,28.736 C22.033,29.004 22.213,29.317 22.721,29.224 C26.903,27.818 30,24.232 30,20 C30,14.477 25.523,10 20,10" fill="{text_color}" />
                        <circle cx="20" cy="20" r="20" fill="none" stroke="url(#accent-gradient)" stroke-width="1.5" opacity="0" filter="url(#soft-glow)">
                            <animate attributeName="opacity" values="0; 0.5; 0" dur="4s" begin="3.5s" repeatCount="indefinite" />
                        </circle>
                    </g>
                    <!-- LinkedIn -->
                    <g transform="translate(60, 0)">
                        <circle cx="20" cy="20" r="20" fill="{border_color}" />
                        <path d="M13.682,27.135 H10.237 V15.753 H13.682 V27.135 Z M11.959,14.204 C10.857,14.204 9.963,13.309 9.963,12.207 C9.963,11.106 10.857,10.211 11.959,10.211 C13.061,10.211 13.955,11.106 13.955,12.207 C13.955,13.309 13.061,14.204 11.959,14.204 Z M30,27.135 H26.558 V21.61 C26.558,20.292 26.533,18.599 24.727,18.599 C22.894,18.599 22.613,20.031 22.613,21.517 V27.135 H19.171 V15.753 H22.482 V17.307 H22.527 C22.989,16.433 24.119,15.522 25.776,15.522 C29.25,15.522 30,17.81 30,20.81 V27.135 Z" fill="{text_color}" />
                        <circle cx="20" cy="20" r="20" fill="none" stroke="url(#accent-gradient)" stroke-width="1.5" opacity="0" filter="url(#soft-glow)">
                            <animate attributeName="opacity" values="0; 0.5; 0" dur="4s" begin="4.5s" repeatCount="indefinite" />
                        </circle>
                    </g>
                    <!-- Twitter -->
                    <g transform="translate(120, 0)">
                        <circle cx="20" cy="20" r="20" fill="{border_color}" />
                        <path d="M22.46,14.172 H25.26 L19.145,21.163 L26.33,30.655 H20.707 L16.305,24.898 L11.267,30.655 H8.465 L14.981,23.21 L8.064,14.172 H13.827 L17.804,19.421 L22.46,14.172 Z M21.479,28.983 H23.031 L12.825,15.753 H11.162 L21.479,28.983 Z" fill="{text_color}" />
                        <circle cx="20" cy="20" r="20" fill="none" stroke="url(#accent-gradient)" stroke-width="1.5" opacity="0" filter="url(#soft-glow)">
                            <animate attributeName="opacity" values="0; 0.5; 0" dur="4s" begin="5.5s" repeatCount="indefinite" />
                        </circle>
                    </g>
                    <!-- Portfolio (Link icon) -->
                    <g transform="translate(180, 0)">
                        <circle cx="20" cy="20" r="20" fill="{border_color}" />
                        <path d="M14 16h-3c-2.76 0-5-2.24-5-5s2.24-5 5-5h3v2h-3c-1.65 0-3 1.35-3 3s1.35 3 3 3h3v2zm9-10h-3v2h3c1.65 0 3 1.35 3 3s-1.35 3-3 3h-3v2h3c2.76 0 5-2.24 5-5s-2.24-5-5-5zm-11 6h8v2h-8z" fill="{text_color}" />
                        <circle cx="20" cy="20" r="20" fill="none" stroke="url(#accent-gradient)" stroke-width="1.5" opacity="0" filter="url(#soft-glow)">
                            <animate attributeName="opacity" values="0; 0.5; 0" dur="4s" begin="6.5s" repeatCount="indefinite" />
                        </circle>
                    </g>
                </g>
            </g>
        </g>
    </g>

    </svg>"""
    return svg

with open("dark.svg", "w", encoding="utf-8") as f:
    f.write(generate_svg("dark"))
    
with open("light.svg", "w", encoding="utf-8") as f:
    f.write(generate_svg("light"))
