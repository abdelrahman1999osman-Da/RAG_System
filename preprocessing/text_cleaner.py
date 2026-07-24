import re


class TextCleaner:

    def clean(self, text: str) -> str:
        if not isinstance(text, str):
            return ""

        # 1. تحويل النص للحروف الصغيرة
        text = text.lower()

        # 2. إزالة الإيميلات ورموز @ المنفردة
        text = re.sub(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", " ", text
        )
        text = re.sub(r"@", " ", text)

        # 3. 🔥 مسح سيل النقاط الطويل واستبداله بنقطتين بس (..)
        # لو فيه 3 نقاط أو أكتر (بينهم مسافات أو لأ)، هيخليهم نقطتين بس
        text = re.sub(r"(?:\.\s*){3,}", ".. ", text)
        text = re.sub(r"\.{3,}", ".. ", text)

        # 4. توحيد الفواصل السطرية (Line breaks) والـ Tabs
        text = re.sub(r"[\r\n\t]+", " ", text)

        # 5. إزالة Control Characters المزعجة
        text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]+", " ", text)

        # 6. الاحتفاظ بالرموز الكيميائية والعلمية والأرقام طبيعية بدون مسح الأرقام
        text = re.sub(r"[^\w\s.,:;!?/()\[\]{}+\%°*'\"-]+", " ", text)

        # 7. تقليص المسافات الزائدة بدون المساس بالنقاط أو الأرقام
        text = re.sub(r"\s+", " ", text)

        return text.strip()