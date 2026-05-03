# Cellular & Synaptic Mechanisms under _in vivo_ Regimes

An important contribution of my past research has been to evaluate cellular mechanisms in the context of *in vivo-like* activity.


%% Fig. [Test.png](../Figures/Test.png)  around here ! %%
**Discrepancy between firing patterns in response to either step protocol stimulation or stochastic fluctuations in single cell models.** From top to bottom we stimulate 4 different parameter configurations of the AdExp model.
**(a)** This is a draft legend. 
**(b)** This is also a draft legend. 


I generate some simulations here base on the Brian2 simulator ([Stimberg et al., 2019](Stimberg2019.pdf))
[Brette & Gerstner, 2005](Brette2005.pdf) 
Single cell equation:
$$
\begin{aligned}
C_m \cdot \frac{d\,V}{dt} & = g_L \cdot (E_L - V) - w_a + I(t)  \\
\tau_a \cdot \frac{d \, w}{d t} = & \, a \, \cdot \, ( w \, - )
\end{aligned}
$$

Some parameters were fixed to $E_L$ =-65mV, $C_m$=200pF, $\tau_w$=200ms, $\tau_{refrac}$=5ms, $V_{reset}$=-65mV. 
The other () were varied as shown in the figure.

I describe below a few scientific contributions that illustrate particularly well my research profile. Notably, I focus on those that show the mixed experimental and theoretical expertise on cortical dynamics that are necessary for the completion of my research project.

 write here a reference to [Fig.](../Figures/Test.png)A




The Spectrum of Asynchronous Dynamics in Spiking Networks as a Model for the Diversity of Non-Rhythmic Waking States in Neocortex [Zerlaut et al., 2019](Zerlaut2019.pdf)


**6. Heterogeneous firing rate response of mouse layer V pyramidal neurons in the fluctuation‐driven regime**  
        [Zerlaut et al., _Journal of Physiology_ (2016)](https://drive.google.com/file/d/1FKILNz_0ustMmVzz0hbp4l8aO6B5B6Xs/view?usp=share_link)

  
This work from my PhD is my first contribution with mixed theoretical and experimental work. I performed both the theoretical analysis (fluctuation regime analysis, deriving the analytical template for the transfer functions, modelling the biophysical properties) and the experimental characterisation (intracellular recordings in perforated patch using the dynamic-clamp technique).

In this study, we recreate in vitro the fluctuation-driven regime observed at the soma during asynchronous network activity in vivo and we studied the firing rate response as a function of the properties of the membrane potential fluctuations. We provide a simple analytical template that captures the firing response of both pyramidal neurons and various theoretical models.  
We found a strong heterogeneity in the firing rate response of layer V pyramidal neurons: in particular, individual neurons differ not only in their mean excitability level, but also in their sensitivity to fluctuations. Theoretical modelling suggests that this observed heterogeneity might arise from various expression levels of the following biophysical properties: sodium inactivation, density of sodium channels and spike frequency adaptation.


**5. Activity-dependent modulation of NMDA receptors by endogenous zinc shapes dendritic function in cortical neurons**  
           [Morabito et al., _Cell Reports_ (2022)](https://drive.google.com/file/d/1VZkrACwY_7LMhrJ67GpCNKR7cyW5b44E/view?usp=share_link)

In my first contribution to the research of the host laboratory, I derived the equations and implemented the numerical simulations for the action of vesicular zinc on synaptic integration in morphologically- and biophysically-detailed neuronal models. 

NMDA receptors (NMDARs) have been proposed to control single-neuron computations in vivo. However, whether specific mechanisms regulate the function of such receptors and modulate input-output transformations performed by cortical neurons under in vivo-like conditions is understudied. In this study, the host laboratory reports that in layer 2/3 pyramidal neurons (L2/3 PNs), repeated synaptic stimulation results in an activity-dependent decrease in NMDAR function by vesicular zinc.

My numerical simulations highlighted that activity-dependent modulation of NMDARs influences dendritic computations, endowing L2/3 PN dendrites with the ability to sustain non-linear integrations constant across different regimes of synaptic activity like those found in vivo. Our results unveil vesicular zinc as an important endogenous modulator of dendritic function in cortical PNs.





