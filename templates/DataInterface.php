<?php

namespace MountainTales\Packing\Api\Data;

use Magento\Framework\Api\ExtensibleDataInterface;

/**
 * Inferface {{ model }}Interface
 * 
 * @api
 * @package MountainTales\Packing\Api\Data
 */
interface {{ model }}Interface extends ExtensibleDataInterface
{
    /**#@+
     * Constants defined for keys of data array
     */
{% for column in columns %}
    const {{ column.name.upper() }} = '{{ column.name }}';
{% endfor %}

    /**#@-*/
    
{% for column in columns %}
    /**
     * Get {{ column.name.replace('_', ' ') }}
     *
     * @return {{ column.type }}|null
     */
    public function get{{ column.pascal }}();

    /**
     * Set {{ column.name.replace('_', ' ') }}
     *
     * @param {{ column.type }} ${{ column.camel }}
     * @return $this
     */
    public function set{{ column.pascal }}(${{ column.camel }});
{% endfor %}
}