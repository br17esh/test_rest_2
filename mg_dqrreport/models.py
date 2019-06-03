from django.db import models


# Create your models here.
class obsinfo(models.Model):
    UID = models.CharField(max_length=200)
    date_obs = models.CharField(max_length=50)
    time_obs = models.CharField(max_length=50)
    date_end = models.CharField(max_length=50)
    time_end = models.CharField(max_length=50)
    obs_id = models.CharField(max_length=50)
    exposure = models.CharField(max_length=50)
    sourceid = models.CharField(max_length=50)
    observer = models.CharField(max_length=50)
    ra_pnt = models.CharField(max_length=50)
    dec_pnt = models.CharField(max_length=50)

    def __str__(self):
        return self.date_obs


class dqrstats(models.Model):
    UID = models.CharField(max_length=200)
    filename_OF = models.CharField(max_length=50)
    filename_FF = models.CharField(max_length=50)
    size_bytes_OF = models.CharField(max_length=50)
    size_bytes_FF = models.CharField(max_length=50)
    size_OF = models.CharField(max_length=50)
    size_FF = models.CharField(max_length=50)
    events_quadA_OF = models.CharField(max_length=50)
    events_quadA_FF = models.CharField(max_length=50)
    events_quadB_OF = models.CharField(max_length=50)
    events_quadB_FF = models.CharField(max_length=50)
    events_quadC_OF = models.CharField(max_length=50)
    events_quadC_FF = models.CharField(max_length=50)
    events_quadD_OF = models.CharField(max_length=50)
    events_quadD_FF = models.CharField(max_length=50)

    def __str__(self):
        return self.filename_OF


class dph(models.Model):
    UID = models.CharField(max_length=200)
    quadA = models.CharField(max_length=200)
    quadB = models.CharField(max_length=200)
    quadC = models.CharField(max_length=200)
    quadD = models.CharField(max_length=200)

    def __str__(self):
        return self.quadA


class countrate(models.Model):
    UID = models.CharField(max_length=200)
    crplot1 = models.CharField(max_length=200)
    crimg1 = models.CharField(max_length=200)
    crplot2 = models.CharField(max_length=200)
    crimg2 = models.CharField(max_length=200)
    crplot3 = models.CharField(max_length=200)
    crimg3 = models.CharField(max_length=200)
    crplot4 = models.CharField(max_length=200)
    crimg4 = models.CharField(max_length=200)
    crplot5 = models.CharField(max_length=200)
    crimg5 = models.CharField(max_length=200)
    crplot6 = models.CharField(max_length=200)
    crimg6 = models.CharField(max_length=200)

    def __str__(self):
        return self.crplot1


class housekeeping(models.Model):
    UID = models.CharField(max_length=200)
    plot1 = models.CharField(max_length=200)
    plot2 = models.CharField(max_length=200)
    plot3 = models.CharField(max_length=200)
    plot4 = models.CharField(max_length=200)
    plot5 = models.CharField(max_length=200)
    plot6 = models.CharField(max_length=200)
    plot7 = models.CharField(max_length=200)
    plot8 = models.CharField(max_length=200)
    plot9 = models.CharField(max_length=200)
    plot10 = models.CharField(max_length=200)
    plot11 = models.CharField(max_length=200)
    plot12 = models.CharField(max_length=200)
    plot13 = models.CharField(max_length=200)
    plot14 = models.CharField(max_length=200)

    def __str__(self):
        return self.plot1


class datainteg(models.Model):
    UID = models.CharField(max_length=200)
    M9_A_BD = models.CharField(max_length=200)
    M9_A_TP = models.CharField(max_length=200)
    M9_A_DP = models.CharField(max_length=200)
    M9_B_BD = models.CharField(max_length=200)
    M9_B_TP = models.CharField(max_length=200)
    M9_B_DP = models.CharField(max_length=200)
    M9_C_BD = models.CharField(max_length=200)
    M9_C_TP = models.CharField(max_length=200)
    M9_C_DP = models.CharField(max_length=200)
    M9_D_BD = models.CharField(max_length=200)
    M9_D_TP = models.CharField(max_length=200)
    M9_D_DP = models.CharField(max_length=200)

    M0_A_BD = models.CharField(max_length=200)
    M0_A_TP = models.CharField(max_length=200)
    M0_A_DP = models.CharField(max_length=200)
    M0_B_BD = models.CharField(max_length=200)
    M0_B_TP = models.CharField(max_length=200)
    M0_B_DP = models.CharField(max_length=200)
    M0_C_BD = models.CharField(max_length=200)
    M0_C_TP = models.CharField(max_length=200)
    M0_C_DP = models.CharField(max_length=200)
    M0_D_BD = models.CharField(max_length=200)
    M0_D_TP = models.CharField(max_length=200)
    M0_D_DP = models.CharField(max_length=200)

    SS_A_BD = models.CharField(max_length=200)
    SS_A_TP = models.CharField(max_length=200)
    SS_A_DP = models.CharField(max_length=200)
    SS_B_BD = models.CharField(max_length=200)
    SS_B_TP = models.CharField(max_length=200)
    SS_B_DP = models.CharField(max_length=200)
    SS_C_BD = models.CharField(max_length=200)
    SS_C_TP = models.CharField(max_length=200)
    SS_C_DP = models.CharField(max_length=200)
    SS_D_BD = models.CharField(max_length=200)
    SS_D_TP = models.CharField(max_length=200)
    SS_D_DP = models.CharField(max_length=200)

    def __str__(self):
        return self.M9_A_BD


class datasat(models.Model):
    UID = models.CharField(max_length=200)
    QA_TS = models.CharField(max_length=200)
    QA_SS = models.CharField(max_length=200)
    QA_SP = models.CharField(max_length=200)
    QB_TS = models.CharField(max_length=200)
    QB_SS = models.CharField(max_length=200)
    QB_SP = models.CharField(max_length=200)
    QC_TS = models.CharField(max_length=200)
    QC_SS = models.CharField(max_length=200)
    QC_SP = models.CharField(max_length=200)
    QD_TS = models.CharField(max_length=200)
    QD_SS = models.CharField(max_length=200)
    QD_SP = models.CharField(max_length=200)

    def __str__(self):
        return self.QA_TS


class noisefrag(models.Model):
    UID = models.CharField(max_length=200)

    QA_S1B = models.CharField(max_length=200)
    QA_B0C = models.CharField(max_length=200)
    QA_B2KC = models.CharField(max_length=200)
    QA_HRB = models.CharField(max_length=200)
    QA_NTT = models.CharField(max_length=200)
    QA_NDT = models.CharField(max_length=200)
    QA_MLC = models.CharField(max_length=200)

    QB_S1B = models.CharField(max_length=200)
    QB_B0C = models.CharField(max_length=200)
    QB_B2KC = models.CharField(max_length=200)
    QB_HRB = models.CharField(max_length=200)
    QB_NTT = models.CharField(max_length=200)
    QB_NDT = models.CharField(max_length=200)
    QB_MLC = models.CharField(max_length=200)

    QC_S1B = models.CharField(max_length=200)
    QC_B0C = models.CharField(max_length=200)
    QC_B2KC = models.CharField(max_length=200)
    QC_HRB = models.CharField(max_length=200)
    QC_NTT = models.CharField(max_length=200)
    QC_NDT = models.CharField(max_length=200)
    QC_MLC = models.CharField(max_length=200)

    QD_S1B = models.CharField(max_length=200)
    QD_B0C = models.CharField(max_length=200)
    QD_B2KC = models.CharField(max_length=200)
    QD_HRB = models.CharField(max_length=200)
    QD_NTT = models.CharField(max_length=200)
    QD_NDT = models.CharField(max_length=200)
    QD_MLC = models.CharField(max_length=200)

    def __str__(self):
        return self.QA_S1B


class pixelprop(models.Model):
    UID = models.CharField(max_length=200)

    PP_QA1_DID = models.CharField(max_length=200)
    PP_QA1_PID = models.CharField(max_length=200)
    PP_QA1_CNT = models.CharField(max_length=200)
    PP_QA1_SG = models.CharField(max_length=200)
    PP_QA2_DID = models.CharField(max_length=200)
    PP_QA2_PID = models.CharField(max_length=200)
    PP_QA2_CNT = models.CharField(max_length=200)
    PP_QA2_SG = models.CharField(max_length=200)
    PP_QA3_DID = models.CharField(max_length=200)
    PP_QA3_PID = models.CharField(max_length=200)
    PP_QA3_CNT = models.CharField(max_length=200)
    PP_QA3_SG = models.CharField(max_length=200)

    PP_QB1_DID = models.CharField(max_length=200)
    PP_QB1_PID = models.CharField(max_length=200)
    PP_QB1_CNT = models.CharField(max_length=200)
    PP_QB1_SG = models.CharField(max_length=200)
    PP_QB2_DID = models.CharField(max_length=200)
    PP_QB2_PID = models.CharField(max_length=200)
    PP_QB2_CNT = models.CharField(max_length=200)
    PP_QB2_SG = models.CharField(max_length=200)
    PP_QB3_DID = models.CharField(max_length=200)
    PP_QB3_PID = models.CharField(max_length=200)
    PP_QB3_CNT = models.CharField(max_length=200)
    PP_QB3_SG = models.CharField(max_length=200)

    PP_QC1_DID = models.CharField(max_length=200)
    PP_QC1_PID = models.CharField(max_length=200)
    PP_QC1_CNT = models.CharField(max_length=200)
    PP_QC1_SG = models.CharField(max_length=200)
    PP_QC2_DID = models.CharField(max_length=200)
    PP_QC2_PID = models.CharField(max_length=200)
    PP_QC2_CNT = models.CharField(max_length=200)
    PP_QC2_SG = models.CharField(max_length=200)
    PP_QC3_DID = models.CharField(max_length=200)
    PP_QC3_PID = models.CharField(max_length=200)
    PP_QC3_CNT = models.CharField(max_length=200)
    PP_QC3_SG = models.CharField(max_length=200)

    PP_QD1_DID = models.CharField(max_length=200)
    PP_QD1_PID = models.CharField(max_length=200)
    PP_QD1_CNT = models.CharField(max_length=200)
    PP_QD1_SG = models.CharField(max_length=200)
    PP_QD2_DID = models.CharField(max_length=200)
    PP_QD2_PID = models.CharField(max_length=200)
    PP_QD2_CNT = models.CharField(max_length=200)
    PP_QD2_SG = models.CharField(max_length=200)
    PP_QD3_DID = models.CharField(max_length=200)
    PP_QD3_PID = models.CharField(max_length=200)
    PP_QD3_CNT = models.CharField(max_length=200)
    PP_QD3_SG = models.CharField(max_length=200)

    def __str__(self):
        return self.PP_QA1_DID


class quadprop(models.Model):
    UID = models.CharField(max_length=200)

    QP_QA1_MN = models.CharField(max_length=200)
    QP_QA1_MD = models.CharField(max_length=200)
    QP_QA1_SG = models.CharField(max_length=200)
    QP_QA2_MN = models.CharField(max_length=200)
    QP_QA2_MD = models.CharField(max_length=200)
    QP_QA2_SG = models.CharField(max_length=200)
    QP_QA3_MN = models.CharField(max_length=200)
    QP_QA3_MD = models.CharField(max_length=200)
    QP_QA3_SG = models.CharField(max_length=200)
    QP_QB1_MN = models.CharField(max_length=200)
    QP_QB1_MD = models.CharField(max_length=200)
    QP_QB1_SG = models.CharField(max_length=200)
    QP_QB2_MN = models.CharField(max_length=200)
    QP_QB2_MD = models.CharField(max_length=200)
    QP_QB2_SG = models.CharField(max_length=200)
    QP_QB3_MN = models.CharField(max_length=200)
    QP_QB3_MD = models.CharField(max_length=200)
    QP_QB3_SG = models.CharField(max_length=200)
    QP_QC1_MN = models.CharField(max_length=200)
    QP_QC1_MD = models.CharField(max_length=200)
    QP_QC1_SG = models.CharField(max_length=200)
    QP_QC2_MN = models.CharField(max_length=200)
    QP_QC2_MD = models.CharField(max_length=200)
    QP_QC2_SG = models.CharField(max_length=200)
    QP_QC3_MN = models.CharField(max_length=200)
    QP_QC3_MD = models.CharField(max_length=200)
    QP_QC3_SG = models.CharField(max_length=200)
    QP_QD1_MN = models.CharField(max_length=200)
    QP_QD1_MD = models.CharField(max_length=200)
    QP_QD1_SG = models.CharField(max_length=200)
    QP_QD2_MN = models.CharField(max_length=200)
    QP_QD2_MD = models.CharField(max_length=200)
    QP_QD2_SG = models.CharField(max_length=200)
    QP_QD3_MN = models.CharField(max_length=200)
    QP_QD3_MD = models.CharField(max_length=200)
    QP_QD3_SG = models.CharField(max_length=200)

    def __str__(self):
        return self.QP_QA1_MN