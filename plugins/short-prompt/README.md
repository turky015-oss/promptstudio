# Short Prompt for Codex

إضافة Codex مستوحاة من موقع [Short Prompt](https://turky015-oss.github.io/promptstudio/) لصناعة برومبتات احترافية للصور والفيديو والإعلانات والخط العربي.

## ما الذي تقدمه؟

- توليد برومبتات تصوير لمنصات Midjourney وGPT Image وNano Banana وLeonardo وIdeogram وGrok وFlux.
- توليد برومبتات فيديو لـ Sora وRunway وVeo وKling وPika وGrok.
- دعم النصوص والخط العربي مع المحافظة على النص المطلوب.
- بناء إعلانات بصرية مهيأة للمنصة والجمهور، ومنها السوق السعودي.
- عمل محلي دون API أو مفاتيح وصول.

## أمثلة داخل Codex

- `سوّ لي برومبت GPT Image لعطر سعودي فاخر على كثبان العلا.`
- `حوّل مشهد سيارة في الرياض وقت المطر إلى برومبت Sora مدته 8 ثوانٍ.`
- `صمم برومبت خط عربي لعبارة "همة حتى القمة" بخط ديواني.`
- `ابنِ لي إعلان إنستقرام لقهوة مختصة يستهدف السوق السعودي.`

## فحص السكربت

```bash
python3 scripts/generate_prompt.py photo --subject "عطر سعودي فاخر"
python3 scripts/generate_prompt.py ad --product "قهوة مختصة" --platform all
```

المطور: Turki AlSultan  
الموقع: https://turky015-oss.github.io/promptstudio/
