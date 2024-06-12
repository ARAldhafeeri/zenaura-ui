from zenaura.client.hydrator.real_dom_adapter import HydratorRealDomAdapter

real_dom_adapter = HydratorRealDomAdapter() 

DOMIsReady = real_dom_adapter.hyd_rdom_wait_for_dom_content_loaded