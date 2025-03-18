def get_template_choices():
    """
    Get the list of template choices for the LLMRouter.
    
    Returns:
    - List of tuples (template, metadata)
    """
    return [
        (
            "I know this might be an unpopular opinion, but I actually prefer cold pizza over hot pizza.",
            {
                "id": "unpopular_opinion",
                "description": "For contrarian but non-controversial views that spark discussion",
                "format": """
                Unpopular Opinion Tweet Formula:
                - Start with "I know this might be an unpopular opinion, but..."
                - State your contrarian view on a common topic
                - Add "Am I the only one?" to encourage engagement
                - Include relevant emoji
                - End with #unpopularopinion
                """
            }
        ),
        (
            "Don't hit snooze – it messes up your schedule. Do get up right away to boost productivity.",
            {
                "id": "dont_do_this_do_that",
                "description": "For comparing negative behaviors with positive alternatives",
                "format": """
                "Don't Do This, Do That" Formula:
                - Start with "Don't" + negative behavior + reason why it's harmful
                - Follow with "Do" + positive alternative + benefit of this approach
                - End with relevant hashtags that match the advice category
                """
            }
        ),
        (
            "These are the best 5 tweets about SEO I read last week:",
            {
                "id": "the_best_something",
                "description": "For creating numbered lists of top items in a category",
                "format": """
                Best [Topic] List Formula:
                - Start with "These are the best [number] [topic] [time period/context]:"
                - List numbered items with ultra-brief descriptions
                - End with "Check 'em out below" to indicate thread continuation
                """
            }
        ),
        (
            "You don't need more time. You need fewer distractions.",
            {
                "id": "dont_need_you_need",
                "description": "For reframing common misconceptions with actual solutions",
                "format": """
                "You don't need, you need" Formula:
                - First line: "You don't need [common perceived solution]"
                - Second line: "You need [actual solution/reframing]"
                """
            }
        ),
        (
            "as a product manager, when your product wins, your team wins...",
            {
                "id": "unspoken_truth",
                "description": "For sharing industry/role-specific insights",
                "format": """
                Unspoken Truth Formula:
                - State role/context (optional): "as a [role/position]"
                - Present hidden reality or overlooked dynamic
                - Keep tone matter-of-fact, not complaining
                - Focus on systemic truths, not personal grievances
                """
            }
        ),
        (
            "Life hack: Just board the plane in group 1...",
            {
                "id": "life_hack",
                "description": "For sharing simple, unconventional tips",
                "format": """
                Life Hack Formula:
                - Start with "Life hack:"
                - Share a simple, unconventional tip
                - Keep it casual and confident
                - Optional: add benefit/outcome
                """
            }
        ),
        (
            "After struggling for years, I discovered...",
            {
                "id": "compelling_story",
                "description": "For sharing transformational narratives with hook, tension, discovery",
                "format": """
                Compelling Story Formula:
                - Hook - Start with attention-grabbing opener that hints at transformation
                - Tension - Present the problem/struggle faced
                - Discovery - Introduce the solution/revelation
                - Call-to-Action - End with engagement prompt
                """
            }
        ),
        (
            "why people never gossip about how you helped them",
            {
                "id": "complaint",
                "description": "For expressing clever frustrations about relatable situations",
                "format": """
                Complaint Formula:
                - Express frustration clearly but cleverly
                - Use relatable situations/behaviors
                - Can be sarcastic but avoid aggressive tone
                - Optional: add humor or wordplay
                """
            }
        ),
        (
            "9 beginner mistakes as a content creator...",
            {
                "id": "beginner_mistakes",
                "description": "For listing common mistakes in a specific role/field",
                "format": """
                Beginner Mistakes Formula:
                - Start with "[X] beginner mistakes as a [role]:"
                - List numbered mistakes (1 to X)
                - End with "And most importantly... [final key mistake]!"
                """
            }
        ),
        (
            "Short-term thinkers vs Long-term builders...",
            {
                "id": "comparison",
                "description": "For contrasting behaviors/traits of different groups",
                "format": """
                Comparison Formula:
                - Group Labels - Define contrasting groups
                - Negative Actions - List behaviors of first group
                - Positive Actions - List behaviors of second group
                - Format - Use parallel structure for contrast
                """
            }
        ),
        (
            "6 ways to get an endless stream of content ideas...",
            {
                "id": "numbered_list",
                "description": "For sharing actionable tips in a numbered format",
                "format": """
                Numbered List Formula:
                - Title - [X] ways to [Y]
                - List - Numbered points with clear actions/tips
                - Optional conclusion or call-to-action
                - Format - Keep points concise and actionable
                """
            }
        ),
        (
            "In one word, what's the biggest thing holding people back...",
            {
                "id": "challenge",
                "description": "For posing engaging questions with constraints",
                "format": """
                Challenge Question Formula:
                - Question - Ask topic-related question
                - Constraint - Add specific limitation (one word, one sentence)
                - Format - Keep constraint clear and engaging
                - Optional - Add context or stakes
                """
            }
        ),
        (
            "First 6 months: $0, Last month: $28,000...",
            {
                "id": "transformation",
                "description": "For sharing before/after progress stories with metrics",
                "format": """
                Before/After Formula:
                - Starting Point - Initial states/metrics
                - Progress Point (optional) - Mid-journey milestone
                - Current State - Present achievement/metrics
                - Lesson - Brief takeaway or advice
                """
            }
        ),
        (
            "Hard Truth: Most parents want their kids...",
            {
                "id": "hidden_truth",
                "description": "For sharing uncomfortable but important insights",
                "format": """
                Hidden Truth Formula:
                - Label - Start with "Hard Truth:" or "Hidden Truth:"
                - Statement - Present uncomfortable/unconventional insight
                - Format - Make it clear and direct
                - Optional - Add brief explanation/example
                """
            }
        )
    ]