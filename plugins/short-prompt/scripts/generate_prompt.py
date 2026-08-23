#!/usr/bin/env python3
"""Deterministic prompt formatter for the Short Prompt Codex plugin."""

from __future__ import annotations

import argparse
import json
import re
from typing import Dict


NEGATIVE = "blurry, low quality, watermark, deformed, misspelled text"


def add(value: str, prefix: str = ", ") -> str:
    return f"{prefix}{value.strip()}" if value and value.strip() else ""


def aspect_from_platform(platform: str) -> str:
    match = re.search(r"\((\d+)x(\d+)\)", platform)
    if not match:
        return "1:1"
    width, height = map(int, match.groups())
    if width > height:
        return "16:9"
    if height > width:
        return "9:16"
    return "1:1"


def photo(a: argparse.Namespace) -> Dict[str, str]:
    styles = a.style or "cinematic"
    colors = a.colors or "natural"
    base = (
        f"{a.subject}. {a.photo_type} photography, {a.angle} camera angle, "
        f"{a.lighting}, shot with {a.camera} and {a.lens}, {styles} style, "
        f"{colors} color palette, {a.quality}{add(a.extras)}"
    )
    neg = a.negative or NEGATIVE
    return {
        "midjourney": f"{base} --ar {a.ratio} --stylize 250 --quality 2\n\n--no {neg}",
        "gptimage": (
            f"Create a {a.photo_type} photograph of {a.subject}.\n\n"
            f"Composition: {a.angle} camera angle\nLighting: {a.lighting}\n"
            f"Camera and lens: {a.camera}, {a.lens}\nVisual style: {styles}\n"
            f"Color palette: {colors}\nOutput quality: {a.quality}\nAspect ratio: {a.ratio}"
            f"{add(a.extras, chr(10) + 'Additional details: ')}\n"
            f"Avoid: {neg}."
        ),
        "nanobanana": f"{base}\n\nStyle: Photo\nAspect Ratio: {a.ratio}\nQuality: Ultra\nNegative: {neg}",
        "leonardo": f"{base}\n\nNegative prompt: {neg}\nAspect Ratio: {a.ratio}\nGuidance Scale: 8\nSteps: 35",
        "ideogram": f"{base}\n\nAspect Ratio: {a.ratio}\nStyle: Photo\nNegative: {neg}",
        "grok": f"Generate a {a.quality} {a.photo_type} photo: {a.subject}. Angle: {a.angle}. Lighting: {a.lighting}. Lens: {a.lens}. Style: {styles}. Colors: {colors}. Ratio: {a.ratio}.{add(a.extras, ' Extra: ')} Avoid: {neg}.",
        "flux": f"{base}\n\n[Parameters]\naspect_ratio: {a.ratio}\nguidance: 3.5\nsteps: 28\nnegative_prompt: {neg}",
    }


def video(a: argparse.Namespace) -> Dict[str, str]:
    base = f"{a.subject}. Camera movement: {a.motion}. Visual style: {a.style}. Duration: {a.duration}. Cinematic quality, smooth coherent motion{add(a.extras)}"
    return {
        "sora": f"{base}. Maintain subject and scene continuity; natural physics; no abrupt cuts.",
        "runway": f"{base}\n\nHigh quality, smooth transitions, controlled camera motion.",
        "veo": f"{base}\n\nUltra HD, professional cinematography, realistic temporal consistency.",
        "kling": f"{base}\n\nHigh-quality video generation, stable details, natural movement.",
        "pika": f"{base}\n\nDynamic but controlled motion, clean transitions, consistent subject.",
        "grok": f"Generate a cinematic video: {base}. Preserve identity, geometry, and lighting across frames.",
    }


def calligraphy(a: argparse.Namespace) -> Dict[str, str]:
    base = (
        f"Arabic calligraphy text \"{a.text}\" written exactly as provided in {a.style} script, "
        f"{a.material}, background: {a.background}, masterful Arabic calligraphy, "
        f"ultra-detailed, balanced composition{add(a.extras)}"
    )
    neg = "blurry, low quality, incorrect text, misspelled text, Latin letters"
    return {
        "midjourney": f"{base} --ar {a.ratio} --stylize 300 --quality 2\n\n--no {neg}",
        "gptimage": f"Create a polished artwork. {base}. Prioritize exact Arabic letterforms and legibility.\n\nAspect ratio: {a.ratio}\nAvoid: {neg}.",
        "nanobanana": f"{base}\n\nStyle: Art\nAspect Ratio: {a.ratio}\nQuality: Ultra\nNegative: {neg}",
        "leonardo": f"{base}\n\nNegative prompt: {neg}\nAspect Ratio: {a.ratio}\nGuidance Scale: 8\nSteps: 35",
        "ideogram": f"{base}. Render the quoted Arabic text exactly, with no added characters.\n\nAspect Ratio: {a.ratio}\nNegative: {neg}",
        "flux": f"{base}\n\n[Parameters]\naspect_ratio: {a.ratio}\nguidance: 4.0\nsteps: 30\nnegative_prompt: {neg}",
    }


def ad(a: argparse.Namespace) -> Dict[str, str]:
    ratio = a.ratio or aspect_from_platform(a.destination)
    copy = f", exact text overlay \"{a.copy}\" in clear modern typography" if a.copy else ", clean layout with intentional space for copy"
    description = add(a.description)
    base = (
        f"Professional {a.ad_type} advertisement for {a.product}{description}. "
        f"Format: {a.destination}. Target audience: {a.audience}. Mood: {a.mood}. "
        f"Color palette: {a.colors}. Lighting: {a.lighting}{copy}{add(a.extras)}. "
        "Commercial photography, polished art direction, brand-ready"
    )
    neg = "blurry, low quality, amateur, watermark, stock photo look, distorted product, misspelled text"
    dimensions = re.search(r"\((\d+x\d+)\)", a.destination)
    size = dimensions.group(1) if dimensions else ratio
    return {
        "midjourney": f"{base} --ar {ratio} --stylize 250 --quality 2\n\n--no {neg}",
        "gptimage": f"Create a professional advertisement image.\n\nProduct: {a.product}{description}\nAd type: {a.ad_type}\nPlatform: {a.destination}\nAudience: {a.audience}\nMood: {a.mood}\nColors: {a.colors}\nLighting: {a.lighting}{add(a.copy, chr(10) + 'Exact text overlay: ')}{add(a.extras, chr(10) + 'Additional details: ')}\n\nCommercial photography, polished art direction, brand-ready.\nSize: {size}\nAvoid: {neg}.",
        "nanobanana": f"{base}\n\nStyle: Commercial Photography\nAspect Ratio: {ratio}\nQuality: Ultra\nNegative: {neg}",
        "leonardo": f"{base}\n\nNegative prompt: {neg}\nAspect Ratio: {ratio}\nGuidance Scale: 8\nSteps: 35",
        "ideogram": f"{base}. Preserve any quoted text exactly.\n\nAspect Ratio: {ratio}\nStyle: Photo\nNegative: {neg}",
        "grok": f"Generate a professional advertisement for {a.product}{description}. Type: {a.ad_type}. Platform: {a.destination}. Audience: {a.audience}. Mood: {a.mood}. Colors: {a.colors}. Lighting: {a.lighting}.{add(a.copy, ' Exact text: ')} Ratio: {ratio}. Avoid: {neg}.",
        "flux": f"{base}\n\n[Parameters]\naspect_ratio: {ratio}\nguidance: 4.0\nsteps: 30\nnegative_prompt: {neg}",
    }


def common_platform(parser: argparse.ArgumentParser, default: str) -> None:
    parser.add_argument("--platform", default=default, help="Platform key or 'all'")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate platform-ready visual prompts.")
    sub = p.add_subparsers(dest="mode", required=True)

    x = sub.add_parser("photo")
    x.add_argument("--subject", required=True)
    x.add_argument("--photo-type", default="studio")
    x.add_argument("--angle", default="eye-level")
    x.add_argument("--lighting", default="soft studio lighting")
    x.add_argument("--camera", default="full-frame camera")
    x.add_argument("--lens", default="50mm lens")
    x.add_argument("--style", default="cinematic")
    x.add_argument("--colors", default="natural")
    x.add_argument("--ratio", default="1:1")
    x.add_argument("--quality", default="ultra-detailed professional")
    x.add_argument("--extras", default="")
    x.add_argument("--negative", default=NEGATIVE)
    common_platform(x, "gptimage")

    x = sub.add_parser("video")
    x.add_argument("--subject", required=True)
    x.add_argument("--motion", default="slow dolly-in")
    x.add_argument("--duration", default="8 seconds")
    x.add_argument("--style", default="cinematic photorealism")
    x.add_argument("--extras", default="")
    common_platform(x, "sora")

    x = sub.add_parser("calligraphy")
    x.add_argument("--text", required=True)
    x.add_argument("--style", default="Diwani")
    x.add_argument("--material", default="gold leaf on dark paper")
    x.add_argument("--background", default="dark elegant gradient")
    x.add_argument("--ratio", default="16:9")
    x.add_argument("--extras", default="")
    common_platform(x, "ideogram")

    x = sub.add_parser("ad")
    x.add_argument("--product", required=True)
    x.add_argument("--description", default="")
    x.add_argument("--ad-type", default="product showcase on an elegant surface")
    x.add_argument("--destination", default="Instagram Post (1080x1080)")
    x.add_argument("--audience", default="Saudi local market audience")
    x.add_argument("--mood", default="premium luxury elegant")
    x.add_argument("--colors", default="black and gold luxury")
    x.add_argument("--lighting", default="professional studio softbox lighting")
    x.add_argument("--copy", default="")
    x.add_argument("--extras", default="")
    x.add_argument("--ratio", default="")
    common_platform(x, "gptimage")
    return p


def main() -> None:
    args = build_parser().parse_args()
    prompts = {"photo": photo, "video": video, "calligraphy": calligraphy, "ad": ad}[args.mode](args)
    if args.platform == "all":
        print(json.dumps(prompts, ensure_ascii=False, indent=2))
        return
    if args.platform not in prompts:
        available = ", ".join(prompts)
        raise SystemExit(f"Unsupported platform '{args.platform}' for {args.mode}. Choose: {available}, all")
    print(prompts[args.platform])


if __name__ == "__main__":
    main()
