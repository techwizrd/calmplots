# Do/Don't guide

## Muted vs saturated

Do:
- Use muted tones (`bluey`, `socks`) for dense multi-series plots.
- Use saturated accents (`heeler`, `bluey10`) for highlights and key comparisons.

Don't:
- Use high-saturation colors for all categories in large faceted views.
- Combine strong fills and strong outlines for every mark.

## Category count strategy

Do:
- 1-6 categories: use `bluey` or `heeler` directly.
- 7-10 categories: use `bluey10`.
- 11+ categories: group by semantics, use grayscale for context, and highlight the important subset.

Don't:
- Expand categorical palettes indefinitely.
- Depend only on hue for meaning when categories become crowded.
