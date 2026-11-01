"""Build reproducible vector wireframes and PNG previews. No mailbox is accessed."""
from pathlib import Path
import math
import fitz
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import toColor as HexColor

OUT = Path(__file__).resolve().parent
INK = '#243447'
MUTED = '#526475'
BLUE = '#225F9C'
PALE = '#EAF2FA'
RED = '#B63545'
ROSE = '#FFF0F1'
GREEN = '#28654B'
MINT = '#EAF5EE'
AMBER = '#7B540D'
CREAM = '#FFF4DC'
BORDER = '#9EADBA'
BG = '#F2F5F8'
W = 1200
XS = (32, 432, 832)
CW = 336


class Drawing:
    def __init__(self, name, height):
        self.name, self.h = name, height
        self.c = canvas.Canvas(str(OUT / (name + '.pdf')), pagesize=(W, height))
        self.c.setTitle(name.replace('_', ' ').title())

    def rect(self, x, y, w, h, fill='white', stroke=BORDER, radius=0):
        self.c.setFillColor(HexColor(fill))
        self.c.setStrokeColor(HexColor(stroke))
        self.c.setLineWidth(1.25)
        if radius:
            self.c.roundRect(x, self.h-y-h, w, h, radius, fill=1, stroke=1)
        else:
            self.c.rect(x, self.h-y-h, w, h, fill=1, stroke=1)

    def text(self, x, y, value, size=22, bold=False, color=INK):
        self.c.setFillColor(HexColor(color))
        self.c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
        self.c.drawString(x, self.h-y-size*.8, value)

    def para(self, x, y, value, width, size=21, color=INK, bold=False, leading=None):
        font = 'Helvetica-Bold' if bold else 'Helvetica'
        leading = leading or size*1.22
        for part in value.split('\n'):
            line = ''
            for word in part.split():
                test = (line+' '+word).strip()
                if pdfmetrics.stringWidth(test, font, size) > width and line:
                    self.text(x, y, line, size, bold, color)
                    y += leading
                    line = word
                else:
                    line = test
            self.text(x, y, line, size, bold, color)
            y += leading
        return y

    def button(self, x, y, value, primary=True, size=20):
        width = pdfmetrics.stringWidth(value, 'Helvetica-Bold', size)+24
        self.rect(x, y, width, 34, BLUE if primary else 'white', BLUE, 3)
        self.text(x+12, y+8, value, size, True, 'white' if primary else BLUE)
        return width

    def underline(self, x, y, value, size=21):
        self.text(x, y, value, size)
        width = pdfmetrics.stringWidth(value, 'Helvetica', size)
        p = self.c.beginPath()
        for i in range(int(width)+1):
            xx, yy = x+i, self.h-y-size-3-math.sin(i*math.pi/5)*1.5
            if i == 0:
                p.moveTo(xx, yy)
            else:
                p.lineTo(xx, yy)
        self.c.setStrokeColor(HexColor(RED))
        self.c.setLineWidth(1.8)
        self.c.drawPath(p)

    def arrow(self, x, y):
        self.c.setStrokeColor(HexColor(BLUE))
        self.c.setLineWidth(2)
        yy = self.h-y
        self.c.line(x, yy, x+30, yy)
        self.c.line(x+30, yy, x+22, yy+6)
        self.c.line(x+30, yy, x+22, yy-6)

    def header(self, title, subtitle):
        self.rect(0, 0, W, self.h, BG, BG)
        self.text(32, 24, title, 30, True)
        self.text(32, 63, subtitle, 20, color=MUTED)

    def window(self, x, y, h, title, tint=PALE):
        self.rect(x, y, CW, h)
        self.rect(x, y, CW, 35, tint)
        self.text(x+12, y+8, title, 20, True)

    def steps(self, y, labels):
        for x, label in zip(XS, labels):
            self.text(x, y, label, 22, True, BLUE)

    def finish(self):
        self.c.save()
        doc = fitz.open(OUT / (self.name+'.pdf'))
        doc[0].get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False).save(OUT / (self.name+'.png'))
        for page in doc:
            for word in page.get_text('words'):
                assert word[0] >= -1 and word[1] >= -1 and word[2] <= page.rect.width+1 and word[3] <= page.rect.height+1, word
        doc.close()


def a_row(d, top, index):
    names = ['A1  Missing attachment', 'A2  Greeting / recipient mismatch', 'A3  Potentially sensitive text']
    d.text(32, top, names[index], 23, True)
    y = top+34
    for x, title in zip(XS, ('Outlook / Compose', 'Outlook / Inline suggestion', 'Outlook / Editable draft')):
        d.window(x, y, 225, title, MINT if x == XS[2] else PALE)
    d.arrow(384, y+100)
    d.arrow(784, y+100)
    x0, x1, x2 = [x+12 for x in XS]
    z = y+48
    if index == 0:
        d.text(x0, z, 'To: alex@example.com', 20)
        d.text(x0, z+30, 'Subject: Project Update', 20)
        d.text(x0, z+65, 'Please see the attached report.', 21)
        d.text(x0, z+100, 'Attachments: none', 21, color=RED)
        d.button(x0, z+136, 'Send')
        d.text(x1, z, 'Please see the', 21)
        d.underline(x1, z+27, 'attached report.')
        d.rect(x1, z+62, 312, 98, ROSE, '#D2A4AB')
        d.para(x1+10, z+70, 'Attachment mentioned, but no file is attached.', 292, 20)
        bw = d.button(x1+10, z+121, 'Attach file', size=18)
        d.button(x1+20+bw, z+121, 'Ignore', False, 18)
        d.text(x2, z, 'To: alex@example.com', 20)
        d.text(x2, z+30, 'Subject: Project Update', 20)
        d.text(x2, z+65, 'Please see the attached report.', 21)
        d.rect(x2, z+100, 312, 34, MINT, '#98B6A2')
        d.text(x2+8, z+108, 'project_report.pdf', 20, color=GREEN)
        d.text(x2, z+145, 'Warning cleared; still editable.', 20, color=GREEN)
    elif index == 1:
        for xx in (x0, x2):
            d.text(xx, z, 'To: alex@example.com,', 20)
            d.text(xx, z+25, 'sam@example.com + 2 others', 20)
        d.text(x0, z+65, 'Hi Alex,', 22)
        d.text(x0, z+100, 'Here is the project update.', 21)
        d.text(x0, z+141, '4 recipients; 1 named greeting', 20, color=MUTED)
        d.text(x1, z, 'Hi ', 22)
        d.underline(x1+26, z, 'Alex', 22)
        d.rect(x1, z+38, 312, 125, ROSE, '#D2A4AB')
        d.para(x1+10, z+46, '4 recipients, but one name in the greeting. Is this intended?', 292, 20)
        bw = d.button(x1+10, z+119, 'Review recipients', size=18)
        d.button(x1+20+bw, z+119, 'Ignore', False, 18)
        d.text(x2, z+65, 'Hi everyone,', 22)
        d.text(x2, z+100, 'Here is the project update.', 21)
        d.text(x2, z+141, 'Recipients reviewed; still editable.', 19, color=GREEN)
    else:
        d.text(x0, z, 'To: alex@example.com', 20)
        d.text(x0, z+32, 'My home address is', 21)
        d.text(x0, z+62, '123 Maple Street, Apt 4.', 21)
        d.text(x0, z+111, 'Fictional address for this task', 20, color=MUTED)
        d.text(x1, z, 'My home address is', 21)
        d.underline(x1, z+28, '123 Maple Street, Apt 4.')
        d.rect(x1, z+63, 312, 98, CREAM, '#C8AE79')
        d.para(x1+10, z+71, 'Possible home address. Review before sharing.', 292, 20)
        bw = d.button(x1+10, z+122, 'Edit text', size=18)
        d.button(x1+20+bw, z+122, 'Ignore', False, 18)
        d.text(x2, z, 'To: alex@example.com', 20)
        d.para(x2, z+38, 'I will share the meeting location separately.', 312, 21)
        d.text(x2, z+108, 'Address removed by user.', 20, color=GREEN)
        d.text(x2, z+141, 'Warning cleared; still editable.', 20, color=GREEN)


def build_a():
    d = Drawing('prototype_a', 1046)
    d.header('A  Inline Pre-Send Error Detection', 'Three independent examples. Read each row left to right; click an underline to see a suggestion.')
    d.steps(106, ('1  Initial draft', '2  User opens warning', '3  Correct / continue editing'))
    for i in range(3):
        a_row(d, 148+i*282, i)
    d.text(32, 1009, 'Proposed: optional on-device text rules; no draft upload for this check. Flags can be wrong.', 20, color=MUTED)
    # Appendix pages enlarge one case at a time, using exactly the same vector artwork.
    d.c.showPage()
    d.h = 420
    d.c.setPageSize((W, d.h))
    for i in range(3):
        d.header('A  Inline Pre-Send Error Detection', 'Independent scenario '+str(i+1)+' / 3. All email details are fictional.')
        a_row(d, 106, i)
        d.text(32, 395, 'Select Ignore to keep the draft; the checker does not choose the intended recipient or decide what is private.', 19, color=MUTED)
        if i < 2:
            d.c.showPage()
    d.finish()

    # Reflow appendix cases as larger vertical sequences, preserving vector text.
    source = fitz.open(OUT / 'prototype_a.pdf')
    enlarged = fitz.open()
    enlarged.insert_pdf(source, from_page=0, to_page=0)
    case_titles = ('Missing attachment', 'Greeting / recipient mismatch', 'Potentially sensitive text')
    step_titles = ('1  Initial draft', '2  Open contextual warning', '3  Correct / continue editing')
    for i, title in enumerate(case_titles):
        page = enlarged.new_page(width=400, height=900)
        page.draw_rect(page.rect, color=None, fill=(.95, .96, .98))
        page.insert_text((32, 27), 'A'+str(i+1)+'  '+title, fontsize=17, fontname='hebo', color=(.14, .20, .28))
        page.insert_text((32, 51), 'Independent case / all details are fictional', fontsize=12)
        for j, xx in enumerate(XS):
            page.insert_text((32, 85+j*250), step_titles[j], fontsize=15, fontname='hebo', color=(.13, .37, .61))
            page.show_pdf_page(fitz.Rect(32, 100+j*250, 368, 325+j*250), source, i+1,
                               clip=fitz.Rect(xx, 140, xx+CW, 365))
        page.insert_text((32, 858), 'Ignore keeps the draft unchanged.', fontsize=13)
        page.insert_text((32, 880), 'Suggestions can be wrong; the user decides.', fontsize=13)
    temp = OUT / 'prototype_a.layout.pdf'
    enlarged.save(temp)
    enlarged.close()
    source.close()
    temp.replace(OUT / 'prototype_a.pdf')


def build_b():
    d = Drawing('prototype_b', 644)
    d.header('B  Configurable Undo Send', 'Choose a delay, send a message, then cancel it while it is pending.')
    d.steps(110, ('1  Configure', '2  Send / pending', '3  Undo / return to draft'))
    for x, title in zip(XS, ('Outlook / Settings', 'Outlook / Pending', 'Outlook / Compose')):
        d.window(x, 152, 384, title, MINT if x == XS[2] else PALE)
    d.arrow(384, 330)
    d.arrow(784, 330)
    x0, x1, x2 = [x+14 for x in XS]
    d.text(x0, 205, 'Undo Send duration', 23, True)
    for yy, label, selected in ((252, '10 seconds', False), (300, '30 seconds', True), (348, '60 seconds', False)):
        if selected:
            d.rect(x0-3, yy-8, 311, 40, PALE, BLUE)
        d.c.setStrokeColor(HexColor(BLUE))
        d.c.setFillColor(HexColor(BLUE if selected else 'white'))
        d.c.circle(x0+12, d.h-yy-10, 8, stroke=1, fill=1)
        d.text(x0+32, yy, label, 22, selected)
    d.para(x0, 402, 'Messages remain pending during this interval.', 306, 22)
    d.button(x0, 480, 'Save')
    d.text(x1, 205, 'Project Update', 23, True)
    d.text(x1, 245, 'To: sam@example.com', 21)
    d.rect(x1, 293, 308, 163, CREAM, '#C8AE79')
    d.text(x1+14, 311, 'Sending in 00:30', 27, True, AMBER)
    d.para(x1+14, 355, 'Pending. Not delivered yet.', 280, 23)
    d.button(x1+14, 408, 'Undo')
    d.text(x1, 485, 'Select Undo before time runs out.', 19, color=MUTED)
    d.text(x2, 205, 'To: sam@example.com', 21)
    d.text(x2, 240, 'Subject: Project Update', 21)
    d.text(x2, 290, 'Hi Sam,', 22)
    d.text(x2, 326, 'Here is the project update.', 21)
    d.text(x2, 367, 'project_report.pdf', 21, color=BLUE)
    d.rect(x2, 411, 308, 64, MINT, '#98B6A2')
    d.text(x2+10, 421, 'Sending canceled.', 22, True, GREEN)
    d.text(x2+10, 451, 'You can edit your message.', 20, color=GREEN)
    d.button(x2, 486, 'Send')
    d.para(32, 564, 'Undo keeps recipients, content, and attachments. If the timer expires, sending proceeds and this Undo window closes.', 1136, 22, MUTED)
    d.text(32, 616, 'Undo cancels a pending send. Recall is a separate attempt after delivery.', 21, color=BLUE)
    d.finish()


def build_c():
    d = Drawing('prototype_c', 922)
    d.header('C  Conditional Recall and Recipient Consent',
             'Proposed rule: within 5 minutes AND unopened = direct recall; otherwise ask the recipient.')
    d.steps(110, ('1  Request recall', '2  Check each recipient', '3A  Both conditions met'))
    for x, title in zip(XS, ('Sender / Sent Items', 'System / Recall eligibility', 'Sender / Direct recall')):
        d.window(x, 152, 258, title, MINT if x == XS[2] else PALE)
    d.arrow(384, 275)
    d.arrow(784, 275)
    x0, x1, x2 = [x+14 for x in XS]
    d.text(x0, 204, 'Project Update', 23, True)
    d.text(x0, 242, 'To: sam@example.com', 21)
    d.text(x0, 276, 'Already delivered', 21)
    d.button(x0, 329, 'Recall message')
    d.text(x1, 204, 'Within 5 minutes?', 23, True)
    d.text(x1, 246, 'AND still unopened?', 23, True)
    d.rect(x1, 289, 308, 90, CREAM, '#C8AE79')
    d.text(x1+12, 300, 'Both yes: recall directly', 21, True, GREEN)
    d.para(x1+12, 333, 'Otherwise: request permission', 284, 21, AMBER)
    d.text(x2, 204, 'Example: 02:00 / unopened', 20, color=MUTED)
    d.rect(x2, 247, 308, 80, MINT, '#98B6A2')
    d.text(x2+12, 263, 'Recall completed', 25, True, GREEN)
    d.text(x2+12, 300, 'Recipient copy removed.', 21, color=GREEN)
    d.text(x2, 352, 'No recipient approval needed.', 20)

    # The otherwise branch returns to the leftmost panel on the second row.
    d.c.setStrokeColor(HexColor(AMBER))
    d.c.setLineWidth(2)
    p = d.c.beginPath()
    p.moveTo(600, d.h-410)
    p.lineTo(600, d.h-444)
    p.lineTo(200, d.h-444)
    p.lineTo(200, d.h-460)
    d.c.drawPath(p)
    d.c.line(200, d.h-460, 194, d.h-450)
    d.c.line(200, d.h-460, 206, d.h-450)
    d.text(35, 430, 'Otherwise', 20, True, AMBER)
    d.text(633, 430, 'Over 5 minutes OR opened', 21, True, AMBER)
    d.steps(473, ('3B  Ask for permission', '4  Recipient chooses', '5  Sender sees outcome'))
    for x, title in zip(XS, ('Sender / Request sent', 'Recipient / Recall request', 'Sender / Possible outcomes')):
        d.window(x, 516, 272, title, CREAM if x != XS[2] else PALE)
    d.arrow(384, 650)
    d.arrow(784, 650)
    d.text(x0, 568, 'Recall request sent', 23, True)
    d.para(x0, 611, 'Waiting for Sam to decide.', 308, 22)
    d.para(x0, 680, 'The original stays visible until approval.', 308, 22, AMBER)
    d.text(x1, 568, 'Taylor asks to recall', 23, True)
    d.text(x1, 605, 'Project Update', 22)
    d.para(x1, 646, 'Allow removal from your mailbox?', 308, 22)
    bw = d.button(x1, 725, 'Allow recall', size=18)
    d.button(x1+bw+10, 725, 'Keep message', False, 18)
    d.text(x2, 568, 'Waiting: original stays', 21, True, AMBER)
    d.text(x2, 617, 'Approved: copy removed', 21, True, GREEN)
    d.text(x2, 666, 'Declined: original stays', 21, True, RED)
    d.para(x2, 718, 'No response: still waiting.', 308, 20, MUTED)
    d.para(32, 822, 'Time starts at delivery. Decisions apply per recipient. Removing a message cannot undo what was already read.', 1136, 22, MUTED)
    d.text(32, 887, 'Concept requires a cooperating mail service; unsupported recipients cannot be promised removal.', 21, color=BLUE)
    d.finish()


if __name__ == '__main__':
    build_a()
    build_b()
    build_c()
    print('Created 3 vector PDFs and 3 matching PNG previews in Figures/.')
