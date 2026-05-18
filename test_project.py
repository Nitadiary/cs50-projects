from project import c_regimen, g_schedule, show_next
from datetime import datetime

def test_c_regimen():
    r = c_regimen("Tylenol", "500 mg", ["12:00", "06:00", "00:00", "18:00"], 2 )
    assert r["drug"] == "Tylenol"
    assert r["dose"] == "500 mg"

def test_g_schedule_length():
    r = c_regimen("Tylenol", "500 mg", ["12:00", "06:00", "00:00", "18:00"], 2 )
    S = g_schedule(r)
    assert len(S) == 8

def test_show_next_print(capsys):
    r = c_regimen("Aspirin", "80 mg", ["20:30"], 1 )
    S = g_schedule(r)
    show_next(S)
    captured = capsys.readouterr()
    assert "next dose" in captured.out
    assert "Aspirin" in captured.out
