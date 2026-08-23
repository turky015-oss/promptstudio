---
name: short-prompt
description: Generate polished, platform-ready prompts for photography, video, Arabic calligraphy, and advertising. Use when the user asks to create, improve, adapt, or translate a visual-generation prompt, mentions Short Prompt, or wants prompts for Midjourney, GPT Image, Nano Banana, Leonardo, Ideogram, Grok, Flux, Sora, Runway, Veo, Kling, or Pika.
---

# Short Prompt

Turn a brief idea into a production-ready visual prompt while preserving the user's intent.

## Workflow

1. Detect the mode: `photo`, `video`, `calligraphy`, or `ad`.
2. Extract details already present. Do not ask for fields that can be inferred safely.
3. Ask at most one concise question only when the subject/product/text itself is missing.
4. Choose the platform the user named. If none was named, default to `gptimage` for images, `sora` for video, and `ideogram` when accurate visible text is central.
5. Run `scripts/generate_prompt.py` from the plugin root when deterministic platform formatting is useful. Otherwise apply the same structure directly.
6. Return the final prompt first in a fenced text block. Follow it with no more than three short notes about assumptions or optional improvements.

## Defaults

- Prompt language: English, unless the user explicitly asks for Arabic output. Arabic subjects, names, and visible copy remain verbatim.
- Photo: cinematic, natural colors, professional quality, 1:1.
- Video: cinematic, slow dolly-in, 8 seconds.
- Calligraphy: Diwani, gold leaf on dark paper, dark elegant gradient, 16:9.
- Ad: Instagram Post (1080x1080), Saudi local audience, premium elegant mood, black and gold, studio lighting.
- Negative prompt: `blurry, low quality, watermark, deformed, misspelled text`.

## Quality rules

- Put the core subject and action first.
- Add composition, camera, lighting, material, color, mood, and output constraints only when useful.
- Keep visible Arabic copy inside quotes and repeat that it must be rendered exactly.
- Do not invent brand claims, prices, discounts, logos, certifications, or product features.
- For ads, distinguish between visual prompt and marketing copy. Preserve supplied copy exactly.
- Avoid contradictory camera, lighting, aspect-ratio, or duration instructions.
- When asked for all platforms, return a clearly labeled prompt per platform; do not blend incompatible platform syntax.
- Do not claim the plugin renders media. It prepares prompts for generation platforms.

## Script usage

Run from the plugin root:

```bash
python3 scripts/generate_prompt.py photo --subject "عطر سعودي فاخر" --platform gptimage
python3 scripts/generate_prompt.py video --subject "سيارة تعبر صحراء العلا" --platform sora
python3 scripts/generate_prompt.py calligraphy --text "همة حتى القمة" --platform ideogram
python3 scripts/generate_prompt.py ad --product "قهوة مختصة" --platform all
```

Use `python3 scripts/generate_prompt.py --help` and the subcommand help for optional fields. The script prints JSON for `--platform all` and plain text for one platform.

## Provenance

This plugin adapts the Short Prompt web experience by Turki AlSultan:
https://turky015-oss.github.io/promptstudio/
